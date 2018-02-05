# -*- coding:utf-8 -*-
from mymodule import Mypickle
from mymodule import Mypath
from mymodule import Server_Mydatabase
import os
import sys



if __name__ == "__main__":

  while(1):
    print("input queryID")i
    
    queryID = input('>>> ')

    if len(Server_Mydatabase.select("SELECT * from query where queryID = \'" + queryID + "\'")) != 0: break
    else: print("\ninput again!!\n\n")

  SQL_seeds = Server_Mydatabase.select("SELECT userID from query where queryID = \'" + queryID + "\'" + "and ID = \'0\'")
  SQL_match = Server_Mydatabase.select("SELECT userID from query where queryID = \'%" + queryID + "%\'" + "and result =  \'2\'")

  seeds = [s[0] for s in SQL_seeds]
  match = list(set([s[0] for s in SQL_match]))

  node2node = {} #{userID:{friend:...,follower:...,friend2friend:...,friend2follower:...,follower2friend:...,follower2follower:...,}}
  nodeofflags = {}
  for u in seeds + match:
    node2node[u] = {}
    nodeofflags[u] = [True, True, True, True, True, True] 

  print("seeds : {0}".format(seeds))
  print("match : {0}".format(match))

  for user in seeds + match:

    if nodeofflags[user][0] and nodeofflags[user][1]:
      friends, followers = Mypath.update("all", user)
      node2node[user]["friend"] = friends
      node2node[user]["follower"] = followers
      nodeofflags[user][0] = False
      nodeofflags[user][1] = False
    elif nodeofflags[user][0] == False and nodeofflags[user][1] == False:
      friends = node2node[user]["friend"]
      followers = node2node[user]["follower"]
    elif nodeofflags[user][0] == False: 
      followers = Mypath.update("followers_only", user)
      node2node[user]["follower"] = followers
      nodeofflags[user][1] = False
      friends = node2node[user]["friend"]
    else:
      friends = Mypath.update("friends_only", user)
      node2node[user]["friend"] =friends 
      nodeofflags[user][0] = False
      followers = node2node[user]["follower"]



    for friend in friends:
      friend2friend, friend2follower = Mypath.update("all", friend)
      ans_friend = list((set(friend2friend) & set(seeds + match)) - set(user))
      ans_follower = list((set(friend2follower) & set(seeds + match)) - set(user))
      node2node[user]["friend2friend"] = []
      node2node[user]["friend2follower"] = []
      for i in ans_friend: node2node[user]["friend2friend"].append([friend, i])
      for i in ans_follower: node2node[user]["friend2follower"].append([friend, i])
      nodeofflags[user][2] = False
      nodeofflags[user][3] = False
  
      if (friend in seed + match):
        
        if nodeofflags[friend][0] = True:
          node2node[friend]["friend"] = friend2friend
          nodeofflags[friend][0] = False
        
        if nodeofflags[friend][1] = True:
        node2node[friend]["follower"] = friend2follower
        nodeofflags[friend][1] = False
 
 
    for follower in followers
      follower2friend, follower2follower = Mypath.update("all", follower)
      ans_friend = list((set(follower2friend) & set(seeds + match)) - set(user))
      ans_follower = list((set(follower2follower) & set(seeds + match)) - set(user))
      node2node[user]["follower2friend"] = []
      node2node[user]["follower2follower"] = []
      for i in ans_friend: node2node[user]["follower2friend"].append([follower, i])
      for i in ans_follower: node2node[user]["follower2follower"].append([follower, i])
      nodeofflags[user][4] = False
      nodeofflags[user][5] = False
  
      if (follower in seed + match):
        
        if nodeofflags[follower][0] = True:
          node2node[follower]["friend"] = follower2friend
          nodeofflags[follower][0] = False
        
        if nodeofflags[follower][1] = True:
        node2node[follower]["follower"] = follower2follower
        nodeofflags[follower][1] = False
  
    
    ans_friend = list((set(friend) & set(seeds + match)) - set(user))
    ans_follower = list((set(follower) & set(seeds + match)) - set(user))
    node2node[user]["friend"] = []
    node2node[user]["follower"] = []
    for i in ans_friend: node2node[user]["friend"].append(i)
    for i in ans_follower: node2node[user]["follower"].append(i)

  Mypickle.save("../query/", node2node)

