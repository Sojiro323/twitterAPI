# -*- coding:utf-8 -*-
from mymodule import Mail
from mymodule import MytwitterAPI
from mymodule import Mypickle
from mymodule import Mypath
from mymodule import Mydatabase
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
path = "../query/"
start_score = 0.1
query_ID = "1"

path_pattern = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",
"25","26","27","28","29","30","31","32","33","34","35","36","37","38","39"]

path_com = {
"1":["1"],
"2":["2"],
"3":["3"],
"4":["4"],
"5":["5"],
"6":["6"],
"7":["1","2","7"],
"8":["2","3","8"],
"9":["1","3","9"],
"10":["3","5","10"],
"11":["3","6","11"],
"12":["2","4","12"],
"13":["1","4","13"],
"14":["4","5","14"],
"15":["4","6","15"],
"16":["2","5","16"],
"17":["1","5","17"],
"18":["2","6","18"],
"19":["1","6","19"],
"20":["1","2","3","7","8","9","20"],
"21":["1","2","4","7","12","13","21"],
"22":["1","2","5","7","16","17","22"],
"23":["1","2","6","7","18","19","23"],
"24":["3","4","5","6","10","11","14","15","24"],
"25":["2","3","5","8","10","16","25"],
"26":["1","3","5","9","10","17","26"],
"27":["2","3","6","8","11","18","27"],
"28":["1","3","6","9","11","19","28"],
"29":["2","4","5","12","14","16","29"],
"30":["1","4","5","13","14","17","30"],
"31":["2","4","6","12","15","18","31"],
"32":["1","4","6","13","15","19","32"],
"33":["1","2","3","5","7","8","9","10","16","17","20","22","25","26","33"],
"34":["1","2","3","6","7","8","9","11","18","19","20","23","27","28","34"],
"35":["1","2","4","5","7","12","13","14","16","17","21","22","29","30","35"],
"36":["1","2","4","6","7","12","13","15","18","19","21","23","31","32","36"],
"37":["2","3","4","5","6","8","10","11","12","14","15","16","18","24","25","27","29","31","37"],
"38":["1","3","4","5","6","9","10","11","13","14","15","17","19","24","26","28","30","32","38"],
"39":path_pattern
}
seeds = ["2294473200","761272495"]
get_num = 10


def recommendation(pattern, seeds, seeds_score):

  print("pattern:{0} recommendation start!!".format(pattern))
  match_list, match_seeds = Mypath.get_match(pattern, seeds)
  print('match_list_lengh is {0}'.format(len(match_list)))
  print(match_list)
  print(match_seeds)


  if len(match_list) == 0: next_pattern = random.choice(path_pattern)
  else:
    match_list = ranking(pattern, match_list, match_seeds, seeds_score)
    print("ranking finish!!")
    match_users, next_pattern, seeds_score = personal_check(pattern, match_list, match_seeds ,seeds_score)
    seeds = seeds + match_users
    print("now seeds is {0}".format(seeds))

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

  match_users = []

  for user in match_list:

    if len(Mydatabase.select('SELECT * from query where userID = \'' + user + '\' AND queryID = \'' + query_ID + '\'')) != 0: continue

    responce = MytwitterAPI.show(user)
    if responce.status_code != 200:
      print("Error code: %d" %(responce.status_code))
      sys.exit()

    ress = json.loads(responce.text)
    print("\nuserID:{0}\nusername:{1}\nprofile:{2}\n".format(user,ress["name"],ress["description"]))

    webbrowser_flag = False
    while(1):
      print("input y or n (help = h)")
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
        ID = Mydatabase.select("SELECT MAX(ID) from query")
        Mydatabase.insert("query", (str(int(ID[0][0]) + 1), userID, query_ID, "2"))
        break
      elif input_flag == "false":
        ID = Mydatabase.select("SELECT MAX(ID) from query")
        Mydatabase.insert("query", (str(int(ID[0][0]) + 1), userID, query_ID, "0"))
        break
      elif input_flag == "half":
        ID = Mydatabase.select("SELECT MAX(ID) from query")
        Mydatavase.insert("query", (str(int(ID[0][0]) + 1), userID, query_ID, "1"))
        break
      else: print("input again!!")

    print("{0} finish!!".format(int(ID[0][0])+1))
    seeds = match_seeds[user]
    if input_flag == "true":
      seeds_score = update_score(input_flag, pattern, seeds, seeds_score)
      seeds_score = init_score(user, seeds_score)
      match_users.append(user)
    else:
      seeds_score = update_score(input_flag, pattern, seeds, seeds_score)

    with open(path + "seeds_score_" + query_ID) as p:
      pickle.dump(seeds_score, p)
      print("save seeds_score")
      print(seeds_score)

    continue_flag, next_pattern = passcheck_continue(pattern, seeds_score)
    if continue_flag: return match_users, next_pattern, seeds_score

  return match_users, next_pattern, seeds_score


def init_score(user, seeds_score):

  user_score = {}
  count = len(seeds_score)

  for seed_k,seed_v in seeds_score.items():
    for path_k, path_v in seed_v.items():
      if path_k not in user_score: user_score[path_k] = [path_v[0]*1.0/count, 0.0, 0.0, 0.0]
      else: user_score[path_k][0] += path_v[0]*1.0/count

  seeds_score[user] = user_score

  return seeds_score


def update_score(flag, pattern, match_seeds, seeds_score):

  p_com = path_com[pattern]

  for seed in match_seeds:
      for p in p_com:
        if flag == "true": seeds_score[seed][p][1] += 1.0
        elif flag == "false": seeds_score[seed][p][3] += 1.0
        else: seeds_score[seed][p][2] += 1.0
        seeds_score[seed][p][0] = seeds_score[seed][p][1] * 1.0 / (seeds_score[seed][p][1] + seeds_score[seed][p][2] + seeds_score[seed][p][3])

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


  if os.path.isfile(path + "seeds_score_" + query_ID):
    seeds_score = Mypickle.load("path", "seeds_score_" + query_ID)
    _, next_pattern = passcheck_continue("0", seeds_score)

  else:
    seeds_score = {}
    for seed in seeds_list:
      seed_score = {p:[start_score,0,0,0] for p in path_pattern}  #[precision, good, bad]
      seeds_score[seed] = seed_score

    next_pattern = random.choice(path_pattern[0:6])

  while(len(seeds_list) < get_num + start_num):
      next_pattern, seeds_list, seeds_score = recommendation(next_pattern, seeds_list, seeds_score)

  visualize(seeds_list[start_num:])
