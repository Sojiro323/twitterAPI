# -*- coding:utf-8 -*-
from connect import database
from mymodule import Myyaml
import recommend

### Execute
if __name__ == "__main__":

  seeds = ['125056081','2294473200','761272495']
  seeds_list = seeds
  start_num = len(seeds_list)
  path = "../query/"
  start_score = 0.6
  query_ID = "3"
  get_num = 30
  path_pattern = Myyaml.load("path")["path_com"]["39"]
  
  while(1):
    print("input using database : old or new")

    d = input('>>> ')

    if d == "new":
      d_flag = True
      break
    elif d == "old":
      d_flag = False
      break
    else: "\ninput again!!\n\n"

  print("query_ID is {0}\n".format(query_ID))

  c_flag = database.select("SELECT * from query where queryID = \'" + query_ID + "\'")
  if len(c_flag) > len(seeds_list):
    from mymodule import Mypickle
    seeds_score = Mypickle.load(path, "seeds_score_" + query_ID)
    _, next_pattern = recommend.passcheck_continue("0", seeds_score)
    seeds_list = [i for i in seeds_score.keys()]

  else:
    seed_score = {p:[start_score,0,0,0] for p in path_pattern}  #[precision, good, bad]
    seeds_score = {i:seed_score for i in seeds_list}
    
    import random
    next_pattern = random.choice(path_pattern[0:6])
    for seed in seeds:database.insert("query", (0, seed, query_ID, "None"))

  while(len(seeds_list) < get_num + start_num):
      next_pattern, seeds_list, seeds_score = recommend.recommendation(d_flag, next_pattern, seeds_list, seeds_score)

  recommend.visualize(seeds_list[start_num:])
