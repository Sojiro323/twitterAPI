#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mymodule import Mail
from mymodule import MytwitterAPI
from mymodule import Mypickle
from mymodule import Mypath
import time
import json
import os
import sys
import random
import itertools
from operator import itemgetter
from selenium import webdriver
#import webbrowser


'''global variable'''
path = "./pickle/"
start_score = 0.1
path_pattern = ["1"]
#path_pattern = ["1","2","3","4","5","6","mutual"]
#derive_pattern = {}
seeds = ["2294473200"]
get_num = 10


def recommendation(pattern, seeds, seeds_score):

  print("pattern:{0} recommendation start!!".format(pattern))
  match_list, match_seeds = Mypath.get_match(pattern, seeds)
  print('match_list_lengh is {0}'.format(len(match_list)))


  if len(match_list) == 0: next_pattern = random.choice(path_pattern)
  else:
    match_list = ranking(pattern, match_list, match_seeds, seeds_score)
    match_users, next_pattern, seeds_score = personal_check(pattern, match_list, match_seeds ,seeds_score)
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

  return ranking_list



def personal_check(pattern, match_list, match_seeds ,seeds_score):

  if os.path.exists(path + "y_n.pickle"): y_n = Mypickle.load(path,'y_n')
  else:y_n = {}
  match_users = []

  for user in match_list:

    if user in y_n: continue

    responce = MytwitterAPI.show(user)
    if responce.status_code != 200:
      print("Error code: %d" %(responce.status_code))
      sys.exit()

    ress = json.loads(responce.text)
    print(user)
    print("username:{1}\nprofile:{2}\n".format(ress["name"],ress["description"]))
    #print("\nuserID:{0}\nusername:{1}\nprofile:{2}\n".format(user,ress["name"],ress["description"]))


    webbrowser_flag = False
    while(1):
      print("input y or n (help = h)")
      input_flag = input('>>>  ')

      '''if input_flag == "h":
        driver = webdriver.Chrome("./chromedriver")
        driver.get("https://twitter.com/intent/user?user_id=" + user)
        webbrowser_flag = True

      elif input_flag == "y" or input_flag == "n":
        y_n[user] = input_flag
        if webbrowser_flag: driver.close()
        break'''


      if input_flag == "y" or input_flag == "n":
        y_n[user] = input_flag

      else: print("input again!!")



    seeds = match_seeds[user]
    if input_flag == "y":
      seeds_score = update_score(True, pattern, seeds, seeds_score)
      seeds_score = init_score(user, seeds_score)
      match_users.append(user)
    else:
      seeds_score = update_score(False, pattern, seeds, seeds_score)

    Mypickle.save(path,y_n)
    continue_flag, next_pattern = passcheck_continue(pattern, seeds_score)
    if continue_flag: return match_users, next_pattern, seeds_score

  return match_users, next_pattern, seeds_score


def init_score(user, seeds_score):

  user_score = {}
  count = len(seeds_score)

  for seed_k,seed_v in seeds_score.items():
    for path_k, path_v in seed_v.items():
      if path_k not in user_score: user_score[path_k] = [path_v[0]*1.0/count, 0.0, 0.0]
      else: user_score[path_k][0] += path_v[0]*1.0/count

  seeds_score[user] = user_score

  return seeds_score


def update_score(flag, pattern, match_seeds, seeds_score):

  for seed in match_seeds:
    if flag: seeds_score[seed][pattern][1] += 1.0
    else: seeds_score[seed][pattern][2] += 1.0
    seeds_score[seed][pattern][0] = seeds_score[seed][pattern][1] * 1.0 / (seeds_score[seed][pattern][1] + seeds_score[seed][pattern][2])

  return seeds_score


def passcheck_continue(pattern, seeds_score):

  score_list = {}
  for seed_k, seed_v in seeds_score.items():
    for path_k, path_v in seed_v.items():
      if path_k not in score_list: score_list[path_k] = path_v[0]
      else:
        score_list[path_k] += path_v[0]

  next_pattern = max(score_list.items(), key=itemgetter(1))[0]

  if next_pattern == pattern: return False, next_pattern
  else: return True, next_pattern


def visualize(answer_list):

  print("visualize")
  print(answer_list)


### Execute
if __name__ == "__main__":

  seeds_list = seeds
  start_num = len(seeds_list)

  seeds_score = {}

  for seed in seeds_list:
    seed_score = {p:[start_score,0,0] for p in path_pattern}  #[precision, good, bad]
    seeds_score[seed] = seed_score

  #next_pattern = random.choice(path_pattern[0:6])
  next_pattern = random.choice(path_pattern)

  while(len(seeds_list) < get_num + start_num):
      next_pattern, seeds_list, seeds_score = recommendation(next_pattern, seeds_list, seeds_score)

  visualize(seeds_list[start_num:])
