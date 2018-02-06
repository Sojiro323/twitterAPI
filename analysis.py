# -*- coding:utf-8 -*-
from mymodule import Mypickle
from mymodule import Mypath
from mymodule import Server_Mydatabase
import os
import sys


path_com = {
1:[1],
2:[2],
3:[3],
4:[4],
5:[5],
6:[6],
7:[1,2],
8:[2,3],
9:[1,3],
10:[3,5],
11:[3,6],
12:[2,4],
13:[1,4],
14:[4,5],
15:[4,6],
16:[2,5],
17:[1,5],
18:[2,6],
19:[1,6],
20:[1,2,3],
21:[1,2,4],
22:[1,2,5],
23:[1,2,6],
24:[3,4,5,6],
25:[2,3,5],
26:[1,3,5],
27:[2,3,6],
28:[1,3,6],
29:[2,4,5],
30:[1,4,5],
31:[2,4,6],
32:[1,4,6],
33:[1,2,3,5],
34:[1,2,3,6],
35:[1,2,4,5],
36:[1,2,4,6],
37:[2,3,4,5,6],
38:[1,3,4,5,6],
39:[1,2,3,4,5,6]
}

def check(2node):

  for v in 2node:  
    if len(v) != 0: return True
  return False



def set_check(2node, opponent, p_dic, path_set):

  SET = []
  users = {}
  
  for k, v in 2node.items():
    if k == "friend" or k == "follower": continue
      for i, u in enumerate(v[:]):
        if u[1] == opponent:
          if u[0] not in users: users[u[0]] = []
            users[u[0]].append(p_dic[k])
            v.pop(i)

  for user in users: SET.append(path_set + user)

  return 2node, SET


      opponent = v.pop(0)
      count[p_dic[k]] += 1
      break

      for k,v in 2node.items():
        count[p_dic[k]] += v.count(opponent)
        2node[k] = list(set[v] - set([opponent])))

      
      ts = [k for k in count.keys() if count[k] != 0]
      j = 1
      for t in ts:
        if t >= 3: j *= count[t]

      for i, p in p_com.items():
      
        if len(set(p) - set(ts)) == 0:
          graph_count[i-1] += j


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
      ans_friend = list((set(friend2friend) & set(seeds + match)) - set([user]))
      ans_follower = list((set(friend2follower) & set(seeds + match)) - set([user]))
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
      ans_friend = list((set(follower2friend) & set(seeds + match)) - set([user]))
      ans_follower = list((set(follower2follower) & set(seeds + match)) - set([user]))
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
  
    
    ans_friend = list((set(friend) & set(seeds + match)) - set([user]))
    ans_follower = list((set(follower) & set(seeds + match)) - set([user]))
    node2node[user]["friend"] = []
    node2node[user]["follower"] = []
    for i in ans_friend: node2node[user]["friend"].append(i)
    for i in ans_follower: node2node[user]["follower"].append(i)

  Mypickle.save("../query/", node2node)

  print("test")
  for node in node2node:
    print(node)
    break

  gpaph_count = [0] * 39
  p_dic = ["friend":1, "follower":2, "friend2follower":3, "follower2friend":4, "friend2follower":5, "follower2follower":6] 

  for user in (seeds + match):

    2node = node2node[user] #dic
    path_set = []

    while(check(2node)):

      while(len(2node["friend"]) != 0 or len(2node["follower"]) != 0):

        if len(2node["friend"]) != 0:
          opponent = 2node["friend"].pop(0)
          path_set.append(1)
          if opponent in 2node["follower"]:
            path_set.append(2)
            2node["follower"].pop(2node["follower"].index(opponent))
        else: 
          opponent = 2node["follower"].pop(0)
          path_set.append(2)

        2node, path_set = set_check(2node, opponent, p_dic, path_set)
  
        for p in path_set:
          for k, com in p_com.items():
            if len(list(set(com) - set(p))) == 0:
              gpaph_count[k-1] += 1

      for k, v in 2node:
        if len(v) != 0:
          opponent = v[1]
          break

      2node, path_set = set_check(2node, opponent, p_dic, [])
      for p in path_set:
        for k, com in p_com.items():
          if len(list(set(com) - set(p))) == 0:
            gpaph_count[k-1] += 1

  Mypickle.save("../query/", graphcount)
