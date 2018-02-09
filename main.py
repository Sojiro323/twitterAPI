# -*- coding:utf-8 -*-
from mymodule import Myyaml
from connect import database
import recommend

### Execute
if __name__ == "__main__":

  seeds = ['75007332','1316932982','261467131']
  seeds_list = seeds
  start_num = len(seeds_list)
  path = "../query/"
  start_score = 0.6
  get_num = 30
  parameter = 0.5
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

  while(1):
    print("input queryID")

    queryID = input('>>> ')
    break


  print("queryID is {0}\n".format(queryID))
  c_flag = database.select("SELECT * from query where queryID = \'" + queryID + "\'")
  if len(c_flag) > len(seeds_list):
    from mymodule import Mypickle
    seeds_score = Mypickle.load(path, "seeds_score_" + queryID)
    _, next_pattern = recommend.passcheck_continue("0", seeds_score)
    seeds_list = [i for i in seeds_score.keys()]

  else:
    seed_score = {p:[start_score,0,0,0] for p in path_pattern}  #[precision, good, bad]
    seeds_score = {i:seed_score for i in seeds_list}
    
    import random
    next_pattern = random.choice(path_pattern)
    for seed in seeds:database.insert("query", (0, seed, queryID, "None"))

  while(len(seeds_list) < get_num + start_num):
      next_pattern, seeds_list, seeds_score = recommend.recommendation(parameter,queryID, d_flag, next_pattern, seeds_list, seeds_score)

  recommend.visualize(seeds_list[start_num:])
