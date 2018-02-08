#!/usr/bin/env python
# -*- coding:utf-8 -*-
from connect import database
from mymodule import Mypickle
import graph
import time
import os


'''global'''
path = "../pickle/"
'''end global'''



### Functions
def main(api):

    #check init or restart
    if os.path.exists(path + "que_" + api + ".pickle"):
      que = load_pickle(api)
    else: que = ["761272495"]

    if api == 'friend': api_flag = 'friends_only'
    else: api_flag = 'followers_only'
    start_time = time.time()

    while(1):

      user = que.pop()

      print("user start : {0}".format(user))
      print(api_flag,user)
      add = graph.update(api_flag, user)

      for ad in add:
        flag = database.check(ad)
        if flag != "protected" and flag != 'NotFound':
          que.insert(0,ad)

      print("que : {0}".format(len(que)))



      end_time = time.time()

      if end_time - start_time > 1800:
        Mypickle.save(path, que, "que_" + api)
        start_time = end_time



def load_pickle(api):

    files = ['que_' + api]
    load_files = Mypickle.load(path,files)

    return load_files[0]



### Execute
if __name__ == "__main__":
  while(1):
    print("input friend or follower")

    api = input('>>> ')

    if api == "friend" or api == 'follower': break
    else: "\ninput again!!\n\n"

  main(api)
