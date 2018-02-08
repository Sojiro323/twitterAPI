#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mymodule import Mail
from mymodule import MytwitterAPI
from mymodule import Mypickle
from mymodule import Server_Mydatabase
from mymodule import Mypath
import time
import json
import os
import sys



'''global'''
path = "../pickle/"
'''end global'''



### Functions
def main(api):

    #check init or restart
    if os.path.exists(path + "pops_" + api + ".pickle"):
      pops = load_pickle(api)
    else: pops = ["761272495"]

    if api == 'friend': api_flag = 'friends_only'
    else: api_flag = 'followers_only'
    start_time = time.time()

    while(1):

      user = pops.pop(0)

      print("user start : {0}".format(user))
      print(api_flag,user)
      add = Mypath.update(api_flag, user)
      
      for ad in add:
        flag = Server_Mydatabase.check(ad)
        if flag != "protected" and flag != 'NotFound':
          pops.append(ad)
      
      print("pops : {0}".format(len(pops)))



      end_time = time.time()

      if end_time - start_time > 1800:
        print("save pickle")
        with open(path + "pops_" + api + ".pickle", mode='wb') as p:
          pickle.dump(pops, p)
        start_time = end_time



def load_pickle(api):

    files = ['pops_' + api]
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
