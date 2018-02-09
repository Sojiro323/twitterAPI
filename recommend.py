# -*- coding:utf-8 -*-
from mymodule import Mypickle
from connect import database
from connect import twitter
from operator import itemgetter
from mymodule import Myyaml
import numpy as np
import itertools
import random
import json
import os
import sys
#from selenium import webdriver
#import webbrowser

'''global variable'''
path = "../query/"
path_pattern = Myyaml.load("path")["path_com"]["39"]




def recommendation(parameter,queryID, d_flag, pattern, seeds, seeds_score):
  if d_flag: import graph
  else: import graph_old as graph

  print("pattern : {0} \n seeds : {1}".format(pattern, seeds))
  match_list, match_seeds = graph.get_match(pattern, seeds)
  print('match_list_lengh : {0}'.format(len(match_list)))


  if len(match_list) == 0: next_pattern = random.choice(path_pattern)
  else:
    af_match_list = ranking(parameter,pattern, match_list, match_seeds, seeds_score)
    match_users, next_pattern, seeds_score = personal_check(queryID, pattern, af_match_list, match_seeds ,seeds_score)

    print("patern next_pattern (seeds:{0}): {1} {2}".format(len(seeds), pattern, next_pattern))
    while(pattern == next_pattern):
      add_match_list, add_match_seeds = graph.get_match(pattern, match_users)
      match_seeds = graph.join_dic([match_seeds, add_match_seeds])
      match_list = list(set(match_list) | set(add_match_list))
      af_match_list = ranking(parameter,pattern, match_list, match_seeds, seeds_score)
      print('all:match_list : {0}'.format(len(match_list)))
      match_users, next_pattern, seeds_score = personal_check(queryID, pattern, af_match_list, match_seeds ,seeds_score)
      print("now seeds : {0}".format(seeds))
      seeds = seeds + match_users

  return next_pattern, seeds, seeds_score


def ranking(parameter,pattern, match_list, match_seeds, seeds_score):

  seeds = seeds_score.keys()
  path_score = {}
  ranking_list = []
  count = 0
  take =300
  if len(match_list) < take: take = len(match_list) -5


  for k,v in seeds_score.items():
    path_score[k] = v[pattern][0]

  for u in match_list:
      s = 0.0
      for seeds in match_seeds[u]: s += path_score[seeds]
      s = (len(match_seeds[u]) * parameter) + ((1-parameter) * s) / len(seeds)
      if count < take:
          ranking_list.append([u,s])
          count+=1
      else:
          if count == take:
              np_list = np.array(ranking_list)
              i = np_list.argmin(0)[1]
              count = take + 1
          if float(np_list[i][1]) < s:
              np_list[i] = [u,s]
              i = np_list.argmin(0)[1]

  vs = np_list.tolist()
  vs.sort(key=lambda x:x[1])
  vs.reverse()
  return vs



def personal_check(queryID, pattern, match_list, match_seeds ,seeds_score):

  match_users = []

  for user in match_list:

    if len(database.select('SELECT * from query where userID = \'' + user[0] + '\' AND queryID = \'' + queryID + '\'')) != 0: continue

    responce = twitter.show(user[0])
    if responce.status_code != 200:
      print("Error code: %d" %(responce.status_code))
      continue

    ress = json.loads(responce.text)
    print("score : {0}".format(user[1]))
    print("\n\nhttps://twitter.com/intent/user?user_id=" + user[0])
    print("screen_name:{0}\nuserID:{1}\nusername:{2}\nprofile:{3}\n".format(ress["screen_name"],user[0],ress["name"],ress["description"]))

    webbrowser_flag = False
    while(1):
      print("input true or false or half (help = h)")
      input_flag = input('>>>  ')

      '''if input_flag == "h":
        driver = webdriver.Chrome("./chromedriver")
        driver.get(":)
        webbrowser_flag = True

      elif input_flag == "y" or input_flag == "n":
        y_n[user] = input_flag
        if webbrowser_flag: driver.close()
        break'''


      if input_flag == "true":
        ID = database.select("SELECT MAX(ID) from query where queryID = \'" + queryID + "\'")
        database.insert("query", (str(int(ID[0][0]) + 1), user[0], queryID, "2"))
        break
      elif input_flag == "false":
        ID = database.select("SELECT MAX(ID) from query where queryID = \'" + queryID + "\'")
        database.insert("query", (str(int(ID[0][0]) + 1), user[0], queryID, "0"))
        break
      elif input_flag == "half":
        ID = database.select("SELECT MAX(ID) from query where queryID = \'" + queryID + "\'")
        Mydatavase.insert("query", (str(int(ID[0][0]) + 1), user[0], queryID, "1"))
        break
      else: print("input again!!")

    print("{0} people checked!!".format(int(ID[0][0])+1))
    seeds = match_seeds[user[0]]
    if input_flag == "true":
      seeds_score = update_score(input_flag, pattern, seeds, seeds_score)
      seeds_score = init_score(user[0], seeds_score)
      match_users.append(user[0])
    else:
      seeds_score = update_score(input_flag, pattern, seeds, seeds_score)

    Mypickle.save(path, seeds_score, "seeds_score_" + queryID)

    continue_flag, next_pattern = passcheck_continue(pattern, seeds_score)
    if continue_flag is True or (continue_flag is False and input_flag == "true"): break

  return match_users, next_pattern, seeds_score


def init_score(user, seeds_score):

  user_score = {}
  count = len(seeds_score)

  for seed_k,seed_v in seeds_score.items():
    for path_k, path_v in seed_v.items():
      if path_k not in user_score: user_score[path_k] = [0.0, 0, 0, 0]
      user_score[path_k][0] += path_v[0]*1.0/count

  seeds_score[user] = user_score
  return seeds_score


def update_score(flag, pattern, match_seeds, seeds_score):

  from mymodule import Myyaml
  match_seeds = list(set(match_seeds))
  path_com = Myyaml.load("path")["path_com"]
  p_com = path_com[pattern]
  print("UPDATE SCORE : {0}".format(match_seeds))
  for seed in match_seeds:
    for p in p_com:
        if flag == "true": seeds_score[seed][p][1] += 1
        elif flag == "false": seeds_score[seed][p][3] += 1
        else: seeds_score[seed][p][2] += 1
        seeds_score[seed][p][0] = seeds_score[seed][p][1] * 1.0 / (seeds_score[seed][p][1] + seeds_score[seed][p][2] + seeds_score[seed][p][3])
  return seeds_score


def passcheck_continue(pattern, seeds_score):

  score_list = {}
  for seed_k, seed_v in seeds_score.items():
    for path_k, path_v in seed_v.items():
      if path_k not in score_list: score_list[path_k] = 0
      score_list[path_k] += path_v[0]/len(seeds_score) * 1.0

  max_val = max(score_list.values())
  keys_of_max_val = [key for key in score_list if score_list[key] == max_val]

  print("now graph pattern score\n {0}\n\n".format(score_list))

  if pattern in keys_of_max_val:
    next_pattern = pattern
  else:
    next_pattern = path_pattern[int(random.choice(keys_of_max_val))-1]

  if next_pattern == pattern: return False, next_pattern
  else: return True, next_pattern


def visualize(answer_list):

  print("visualize")
  print(answer_list)
