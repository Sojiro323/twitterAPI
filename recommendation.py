#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mymodule import Mail
from mymodule import MytwitterAPI
from mymodule import Mypickle
import time
import json
import os
import sys
import random
import itertools
from operator import itemgetter

'''global variable'''
path = "./pickle/"
start_score = 0.1
path_pattern = ["0","1","2"]
seeds = ["2294473200"]
get_num = 10



def recommendation(pattern, seeds, seeds_score):

  print("pattern:{0} recommendation start!!".format(pattern))
  match_list, match_seeds = follow_the_path(pattern, seeds)
  print('match_list_lengh is {0}'.format(len(match_list)))
  
  
  if len(match_list) == 0: next_pattern = random.choice(path_pattern)  
  else:
    match_list = ranking(pattern, match_list, match_seeds, seeds_score)
    match_users, next_pattern, seeds_score = personal_check(pattern, match_list, match_seeds ,seeds_score)
    seeds = seeds + match_users

  print("next pattern is {0}".format(next_pattern))
  return next_pattern, seeds, seeds_score



def follow_the_path(pattern, seeds):

  load_files = Mypickle.load(path, ['friends_dic','followers_dic'])
  friends_dic = load_files[0]
  followers_dic = load_files[1]

  match_list = []
  match_seeds = {}

  if pattern is path_pattern[0]:

    for seed in seeds:
      if seed not in friends_dic or seed not in followers_dic: continue
      friends = friends_dic[seed]
      followers = followers_dic[seed]
      temp = list(set(friends) & set(followers))
      match_list = list(set(match_list) | set(temp))
      for match in match_list:
        if match not in match_seeds: match_seeds[match] = [seed]
        else: match_seeds[match] = match_seeds[match].append(seed)
    
  elif pattern is path_pattern[1]:

    for seed in seeds:
      if seed not in friends_dic: continue
      friends = friends_dic[seed]
      for friend in friends:
        if friend not in friends_dic: continue
        temp = friends_dic[friend] 
        match_list = list(set(match_list) & set(temp))
        for match in match_list:
          if match not in match_seeds: match_seeds[match] = [seed]
          else: match_seeds[match] = match_seeds[match].append(seed)
              
     
  elif pattern is path_pattern[2]:

    for seed in seeds:
      if seed not in followers_dic: continue
      followers = followers_dic[seed]
      for follower in followers:
        if follower not in followers_dic: continue
        temp = followers_dic[follower] 
        match_list = list(set(match_list) & set(temp))
        for match in match_list:
          if match not in match_seeds: match_seeds[match] = [seed]
          else: match_seeds[match] = match_seeds[match].append(seed)
 
  else:
    print("key is not exist")

  return match_list, match_seeds


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
    
  match_users = []

  for user in match_users:
    while(1):
      print(user)
      print("input y or n")
      input_flag = raw_input('>>>  ')
      if input_flag == "y" or input_flag == "n": break
      print("input again!!")

    seeds = match_seeds[user]
    if input_flag == "y":
      seeds_score = update_score(True, pattern, seeds, seeds_score)
      seeds_score = init_score(user, seeds_score)
      match_users.append(user)
    else:
      seeds_score = update_score(False, pattern, seeds, seeds_score)

    continue_flag, next_pattern = check_continue(pattern, seeds_score)
    if continue_flag: return match_users, next_pattern, seeds_score

  return match_users, next_pattern, seeds_score


def init_score(user, seeds_score):

  user_score = {}

  for seed_k,seed_v in seeds_score.items():
    for path_k, path_v in seed_v.items():
      if path_k not in user_score: user_score[path_k] = [path_v, 0, 0]
      else: user_score[path_k][0] += path_v

  seeds_score[user] = user_score
    
  return seeds_score


def updata_score(flag, pattern, match_seeds, seeds_score):

  for seed in match_seeds:
    if flag: seeds_score[seed][pattern][1] += 1
    else: seeds_score[seed][pattern][2] += 1
    seeds_score[seed][pattern][0] = seeds_score[seed][pattern][1] * 1.0 / (seeds_score[seed][pattern][1] + seeds_score[seed][pattern][2])

  return seeds_score


def passcheck_continue(pattern, seeds_score):

  score_list = {}
  for seed_k, seed_v in seeds_score.items():
    for path_k, path_v in seed_v.items():
      if path_k not in score_list: score_list[path_k] = path_v
      else: score_list[path_k] += path_v

  l = sorted(score_list.items(), key=lambda x: x[1])

  if l[-1][0] == pattern: return False, l[-1][0]
  else: return True, l[-1][0]


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

  #next_pattern = random.choice(path_pattern)
  next_pattern = path_pattern[0]

  while(len(seeds_list) < get_num + start_num):
      next_pattern, seeds_list, seeds_score = recommendation(next_pattern, seeds_list, seeds_score)
      print("now seeds : {0}".format(len(seeds_list)-start_num))
      print(seeds_list)

  visualize(seeds_list[start_num:])
