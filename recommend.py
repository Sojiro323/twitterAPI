# -*- coding:utf-8 -*-
from mymodule import Mypickle
from connect import database
from connect import twitter
from operator import itemgetter
import itertools
import random
import json
import os
import sys
#from selenium import webdriver
#import webbrowser

'''global variable'''
path = "../query/"
start_score = 0.6
query_ID = "3"
seeds = ['125056081','2294473200','761272495']

path_pattern = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",
"25","26","27","28","29","30","31","32","33","34","35","36","37","38","39"]



#seeds = ["2294473200","761272495"]
get_num = 10


def recommendation(d_flag, pattern, seeds, seeds_score):
  if d_flag: import graph
  else: import graph_old as graph

  print("pattern : {0}".format(pattern))
  if d_flag: match_list, match_seeds = graph.get_match(pattern, seeds)
  else: match_list, match_seeds = graph_old.get_match(pattern, seeds)
  print('match_list_lengh : {0}'.format(len(match_list)))


  if len(match_list) == 0: next_pattern = random.choice(path_pattern)
  else:
    match_list = ranking(pattern, match_list, match_seeds, seeds_score)
    match_users, next_pattern, seeds_score = personal_check(pattern, match_list, match_seeds ,seeds_score)

    while(pattern == next_pattern):
      add_match_list, add_match_seeds = graph.get_match(pattern, match_users)
      match_seeds = graph.join_dic([match_seeds, add_match_seeds])
      match_list = list(set(match_list) & set(add_match_list))
      match_list = ranking(pattern, match_list, match_seeds, seeds_score)
      match_users, next_pattern, seeds_score = personal_check(pattern, match_list, match_seeds ,seeds_score)

    print("now seeds : {0}".format(seeds))
    seeds = seeds + match_users

  return next_pattern, seeds, seeds_score


def ranking(pattern, match_list, match_seeds, seeds_score):

  seeds = seeds_score.keys()
  path_score = {}
  ranking_list = []

  for k,v in seeds_score.items():
    path_score[k] = v[pattern][0]

  for t in range(len(seeds), 0, -1):
    combinations = []
    temp = list(itertools.combinations(seeds, t))
    for tem in temp: combinations.append(list(tem))
    for i, com in enumerate(combinations):
      sum_score = 0.0
      for c in com: sum_score += path_score[c]
      combinations[i].append(sum_score)
    combinations.sort(key=itemgetter(-1))

    while(len(combinations) > 0):
      c = combinations.pop(-1)[:-1]
      for match in match_list[:]:
        if len(set(c).symmetric_difference(match_seeds[match])) == 0:
          ranking_list.append(match)
          match_list.remove(match)
    if t == len(seeds): print("best combination is \n {0}".format(ranking_list))
    if len(ranking_list) == 100: break

  return ranking_list



def personal_check(pattern, match_list, match_seeds ,seeds_score):

  match_users = []

  for user in match_list:

    if len(database.select('SELECT * from query where userID = \'' + user + '\' AND queryID = \'' + query_ID + '\'')) != 0: continue

    responce = twitter.show(user)
    if responce.status_code != 200:
      print("Error code: %d" %(responce.status_code))
      sys.exit()

    ress = json.loads(responce.text)
    print("https://twitter.com/intent/user?user_id=" + user)
    print("\nuserID:{0}\nusername:{1}\nprofile:{2}\n".format(user,ress["name"],ress["description"]))

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
        ID = database.select("SELECT MAX(ID) from query where queryID = \'" + query_ID + "\'")
        database.insert("query", (str(int(ID[0][0]) + 1), user, query_ID, "2"))
        break
      elif input_flag == "false":
        ID = database.select("SELECT MAX(ID) from query where queryID = \'" + query_ID + "\'")
        database.insert("query", (str(int(ID[0][0]) + 1), user, query_ID, "0"))
        break
      elif input_flag == "half":
        ID = database.select("SELECT MAX(ID) from query where queryID = \'" + query_ID + "\'")
        Mydatavase.insert("query", (str(int(ID[0][0]) + 1), user, query_ID, "1"))
        break
      else: print("input again!!")

    print("{0} people checked!!".format(int(ID[0][0])+1))
    seeds = match_seeds[user]
    if input_flag == "true":
      seeds_score = update_score(input_flag, pattern, seeds, seeds_score)
      seeds_score = init_score(user, seeds_score)
      match_users.append(user)
    else:
      seeds_score = update_score(input_flag, pattern, seeds, seeds_score)

    Mypickle.save(path, seeds_score, "seeds_score_" + query_ID)

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
