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



def check(node):

  for v in node:  
    if len(v) != 0: return True
  return False



def set_check(node, opponent, p_dic, path_set):

  SET = []
  users = {}
  
  for k, v in node.items():
    if k == "friend" or k == "follower": continue
    for i, u in enumerate(v[:]):
      if u[1] == opponent:
        if u[0] not in users: users[u[0]] = []
        users[u[0]].append(p_dic[k])
        v.pop(i)

  for user in users: SET.append(path_set + user)

  return node, SET



if __name__ == "__main__":

  while(1):
    print("input queryID")
    
    queryID = input('>>> ')

    if len(Server_Mydatabase.select("SELECT * from query where queryID = \'" + queryID + "\'")) != 0: break
    else: print("\ninput again!!\n\n")

  SQL_seeds = Server_Mydatabase.select("SELECT userID from query where queryID = \'" + queryID + "\'" + "and ID = \'0\'")
  SQL_match = Server_Mydatabase.select("SELECT userID from query where queryID LIKE \'%" + queryID + "%\'" + "and result =  \'2\'")


  seeds = [s[0] for s in SQL_seeds]
  match = list(set([s[0] for s in SQL_match]))

  node2node = {} #{userID:{friend:...,follower:...,friend2friend:...,friend2follower:...,follower2friend:...,follower2follower:...,}}
  nodeofflags = {}
  for u in seeds + match:
    node2node[u] = {}
    nodeofflags[u] = [True, True] 

  print("seeds : {0}".format(seeds))
  print("match : {0}".format(match))

  for user in seeds + match:

    print("user : {0} start".format(user))

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

    print("friend follower finish : {0} {1}".format(len(friends),len(follower)))

    for friend in friends:
      friend2friend, friend2follower = Mypath.update("all", friend)
      ans_friend = list((set(friend2friend) & set(seeds + match)) - set([user]))
      ans_follower = list((set(friend2follower) & set(seeds + match)) - set([user]))
      node2node[user]["friend2friend"] = []
      node2node[user]["friend2follower"] = []
      for i in ans_friend: node2node[user]["friend2friend"].append([friend, i])
      for i in ans_follower: node2node[user]["friend2follower"].append([friend, i])
  
      if (friend in seeds + match):
        
        if nodeofflags[friend][0] == True:
          node2node[friend]["friend"] = friend2friend
          nodeofflags[friend][0] = False
        
        if nodeofflags[friend][1] == True:
          node2node[friend]["follower"] = friend2follower
          nodeofflags[friend][1] = False
 
      
    print("friends finish : {0} {1}".format(len(friend2friend),len(friend2follower)))

 
    for follower in followers:
      follower2friend, follower2follower = Mypath.update("all", follower)
      ans_friend = list((set(follower2friend) & set(seeds + match)) - set([user]))
      ans_follower = list((set(follower2follower) & set(seeds + match)) - set([user]))
      node2node[user]["follower2friend"] = []
      node2node[user]["follower2follower"] = []
      for i in ans_friend: node2node[user]["follower2friend"].append([follower, i])
      for i in ans_follower: node2node[user]["follower2follower"].append([follower, i])
  
      if (follower in seeds + match):
        
        if nodeofflags[follower][0] == True:
          node2node[follower]["friend"] = follower2friend
          nodeofflags[follower][0] = False
        
        if nodeofflags[follower][1] == True:
          node2node[follower]["follower"] = follower2follower
          nodeofflags[follower][1] = False
  
    print("followers finish : {0} {1}".format(len(follower2friend),len(follower2follower)))
    
    
    ans_friend = list((set(friend) & set(seeds + match)) - set([user]))
    ans_follower = list((set(follower) & set(seeds + match)) - set([user]))
    node2node[user]["friend"] = []
    node2node[user]["follower"] = []
    for i in ans_friend: node2node[user]["friend"].append(i)
    for i in ans_follower: node2node[user]["follower"].append(i)

    print("friend : {0}\nfollower : {1}\nfriend2friend : {2}\nfriend2follower : {3}\n follower2friend : {4}\nfollower2follwoer{5}".format(node2node[user]["friend"],node2node[user]["follower"],node2node[user]["friend2friend"], node2node[user]["friend2follower"], node2node[user]["follower2friend"], node2node[user]["follower2follower"]))

  Mypickle.save("../query/", node2node)

  gpaph_count = [0] * 39
  p_dic = {"friend":1, "follower":2, "friend2follower":3, "follower2friend":4, "friend2follower":5, "follower2follower":6}

  for user in (seeds + match):

    node = node2node[user] #dic
    path_set = []

    while(check(node)):

      while(len(node["friend"]) != 0 or len(node["follower"]) != 0):

        if len(node["friend"]) != 0:
          opponent = node["friend"].pop(0)
          path_set.append(1)
          if opponent in node["follower"]:
            path_set.append(2)
            node["follower"].pop(node["follower"].index(opponent))
        else: 
          opponent = node["follower"].pop(0)
          path_set.append(2)

        node, path_set = set_check(node, opponent, p_dic, path_set)
        print("1 or 2 in set : {0}".format(path_set))
        print("graph_count old : {0}".format(graph_count))

        for p in path_set:
          for k, com in p_com.items():
            if len(list(set(com) - set(p))) == 0:
              gpaph_count[k-1] += 1

        print("graph_count now : {0}".format(graph_count))

      for k, v in node:
        if len(v) != 0:
          opponent = v[1]
          break

      node, path_set = set_check(node, opponent, p_dic, [])
      print("1 or 2 not in set : {0}".format(path_set))
      print("graph_count old : {0}".format(graph_count))

      for p in path_set:
        for k, com in p_com.items():
          if len(list(set(com) - set(p))) == 0:
            gpaph_count[k-1] += 1
      
      print("graph_count now : {0}".format(graph_count))

  Mypickle.save("../query/", graphcount)
