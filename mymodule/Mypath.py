from mymodule import Mydatabase
from mymodule import MytwitterAPI
import sys
import time
import datetime
path_pattern = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39"]



def get_match(pattern, seeds):

  if pattern is path_pattern[0]:#friend
    match_list, match_seeds = basic_pass1(seeds)
    match_seeds = join_dic([match_seeds])

  elif pattern is path_pattern[1]:#follower
    match_list, match_seeds = basic_pass2(seeds)
    match_seeds = join_dic([match_seeds])

  elif pattern is path_pattern[2]:#com_friend
    match_list, match_seeds = basic_pass3(seeds)
    match_seeds = join_dic([match_seeds])

  elif pattern is path_pattern[3]:#com_follower
    match_list, match_seeds = basic_pass4(seeds)
    match_seeds = join_dic([match_seeds])

  elif pattern is path_pattern[4]:#friend_friend
    match_list, match_seeds = basic_pass5(seeds)
    match_seeds = join_dic([match_seeds])

  elif pattern is path_pattern[5]:#follower_follower
    match_list, match_seeds = basic_pass5(seeds)
    match_seeds = join_dic([match_seeds])

  elif pattern is path_pattern[6]:#mutual
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[7]:#8
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass3(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[8]:#9
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass3(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[9]:#10
    list1, seeds1 = basic_pass3(seeds)
    list2, seeds2 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[10]:#11
    list1, seeds1 = basic_pass3(seeds)
    list2, seeds2 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[11]:#12
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass4(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[12]:#13
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass4(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[13]:#14
    list1, seeds1 = basic_pass4(seeds)
    list2, seeds2 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[14]:#15
    list1, seeds1 = basic_pass4(seeds)
    list2, seeds2 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[15]:#16
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[16]:#17
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[17]:#18
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[18]:#19
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2))
    match_seeds = join_dic([seeds1, seeds2])

  elif pattern is path_pattern[19]:#20
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass3(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[20]:#21
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass4(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[21]:#22
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[22]:#23
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[23]:#24
    list1, seeds1 = basic_pass3(seeds)
    list2, seeds2 = basic_pass4(seeds)
    list3, seeds3 = basic_pass5(seeds)
    list4, seeds4 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3) & set(list4))
    match_seeds = join_dic([seeds1, seeds2, seeds3, seeds4])

  elif pattern is path_pattern[24]:#25
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass3(seeds)
    list3, seeds3 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[25]:#26
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass3(seeds)
    list3, seeds3 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[26]:#27
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass3(seeds)
    list3, seeds3 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[27]:#28
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass3(seeds)
    list3, seeds3 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[28]:#29
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass4(seeds)
    list3, seeds3 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[29]:#30
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass4(seeds)
    list3, seeds3 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[30]:#31
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass4(seeds)
    list3, seeds3 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[31]:#32
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass4(seeds)
    list3, seeds3 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3))
    match_seeds = join_dic([seeds1, seeds2, seeds3])

  elif pattern is path_pattern[32]:#33
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass3(seeds)
    list4, seeds4 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2) & set(list3) & set(list4))
    match_seeds = join_dic([seeds1, seeds2, seeds3, seeds4])

  elif pattern is path_pattern[33]:#34
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass3(seeds)
    list4, seeds4 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3) & set(list4))
    match_seeds = join_dic([seeds1, seeds2, seeds3, seeds4])

  elif pattern is path_pattern[34]:#35
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass4(seeds)
    list4, seeds4 = basic_pass5(seeds)
    match_list = list(set(list1) & set(list2) & set(list3) & set(list4))
    match_seeds = join_dic([seeds1, seeds2, seeds3, seeds4])

  elif pattern is path_pattern[35]:#36
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass4(seeds)
    list4, seeds4 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3) & set(list4))
    match_seeds = join_dic([seeds1, seeds2, seeds3, seeds4])

  elif pattern is path_pattern[36]:#37
    list1, seeds1 = basic_pass2(seeds)
    list2, seeds2 = basic_pass3(seeds)
    list3, seeds3 = basic_pass4(seeds)
    list4, seeds4 = basic_pass5(seeds)
    list5, seeds5 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3) & set(list4) & set(list5))
    match_seeds = join_dic([seeds1, seeds2, seeds3, seeds4, seeds5])

  elif pattern is path_pattern[37]:#38
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass3(seeds)
    list3, seeds3 = basic_pass4(seeds)
    list4, seeds4 = basic_pass5(seeds)
    list5, seeds5 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3) & set(list4) & set(list5))
    match_seeds = join_dic([seeds1, seeds2, seeds3, seeds4, seeds5])

  elif pattern is path_pattern[38]:#39
    list1, seeds1 = basic_pass1(seeds)
    list2, seeds2 = basic_pass2(seeds)
    list3, seeds3 = basic_pass3(seeds)
    list4, seeds4 = basic_pass4(seeds)
    list5, seeds5 = basic_pass5(seeds)
    list6, seeds6 = basic_pass6(seeds)
    match_list = list(set(list1) & set(list2) & set(list3) & set(list4) & set(list5) & set(list6))
    match_seeds = join_dic([seeds1, seeds2, seeds3, seeds4, seeds5, seeds6])

  else:
    print("key error")




  return match_list, match_seeds


def match(seed, match_list, match_seeds):

  if len(match_list) == 0:
    return match_seeds

  for match in match_list:
    if match not in match_seeds: match_seeds[match] = [seed]
    else: match_seeds[match] = match_seeds[match].append(seed)

  return match_seedsa

def update(flag, goal, userID):

  friends = []
  followers = []

  if goal == 'all':
    if flag == '***':
      friends = use_API(userID, 'friends')
      followers = use_API(userID, 'followers')
    elif flag == 'followers_only':
      friends = use_API(userID, 'friends')
      followers = Mydatabase.select('select userID from follow_graph where followerID = \'' + userID + '\'')
    elif flag == 'friends_only':
      followers == use_API(userID, 'followers')
      friends = Mydatabase.select('select followerID from follow_graph where userID = \'' + userID + '\'')

    Mydatabase.update(checked_list, (userID, 'all', userID))
    return friends, followers

  elif goal == 'friends_only':
    friends = use_API(userID, 'friends')
    if flag == 'followers_only': Mydatabase.update('checked_list', (userID, 'all', userID))
    else: Mydatabase.update('checked_list', (userID, 'friends_only', userID))

    return friends

  elif goal == 'followers_only':
    followers = use_API(userID, 'followers')
    if flag == 'friends_only': Mydatabase.update('checked_list', (userID, 'all', userID))
    else: Mydatabase.update('checked_list', (userID, 'followers_only', userID))

    return followers


def use_API(userID, api):

  values = []
  if api == 'friends':
    return_list = acsessAPI(userID, 'friends')
    for friend in return_list:
      values.append((userID, friend))
    Mydatabase.insert("follow_graph", values)

  else:
    return_list = acsessAPI(userID, 'followers')
    for follower in return_list:
      values.append((follower, userID))
    Mydatabase.insert("follow_graph", values)

  return return_list


def acsessAPI(userID, api):

    return_list = []

    tmp = Mydatabase.select('select limited, last_use from api_limit where api_name = \'' + api + '\'')
    limit = tmp[0][0]
    last_use = tmp[0][1]
    last_time = datetime.datetime(int(last_use[0:4]),int(last_use[5:7]),int(last_use[8:10]),int(last_use[11:13]),int(last_use[14:16]),int(last_use[17:19]))

    now = time.strftime('%Y-%m-%d %H:%M:%S')
    now_time = datetime.datetime(int(now[0:4]),int(now[5:7]),int(now[8:10]),int(now[11:13]),int(now[14:16]),int(now[17:19]))
    delta = now_time - last_time

    if limit == 0:
      print("start sleep")
      while(delta.total_seconds() < 900):
        now_time = datetime.datetime(int(now[0:4]),int(now[5:7]),int(now[8:10]),int(now[11:13]),int(now[14:16]),int(now[17:19]))
        delta = now_time - last_time

    if api == "followers":responce = MytwitterAPI.followers(userID)
    else:responce = MytwitterAPI.friends(userID)


    limit = int(responce.headers['x-rate-limit-remaining']) if 'x-rate-limit-remaining' in responce.headers else 0
    Mydatabase.update('api_limit', (api, limit, now, api))

    if responce.status_code != 200:
      print("Error code: %d" %(responce.status_code))
      if responce.status_code == 401:
        Mydatabase.update('checked_list', (userID, 'protected', userID))
      elif responce.status_code == 404:
        Mydatabase.update('checked_list', (userID, 'NotFound', userID))



    IDs = json.loads(responce.text)
    for ID in IDs["ids"]:
        return_list.append(ID)

    return return_list


def tuple2list(tp):
  ans = []
  for t in tp:
    ans.append(t[0])
  return ans


def basic_pass1(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    flag = Mydatabase.check(seed)
    if flag == "***" or flag == "followers_only":
      friends = update(flag, 'friends_only', seed)
    elif flag == "friends_only" or flag == "all":
      friends = Mydatabase.select("select followerID from follow_graph where userID = \'" + seed + "\'")
      friends = tuple2list(friends)
    else: continue

    match_list = list(set(match_list) | set(friends))
    match_seeds = match(seed, friends, match_seeds)
    print(len(match_list), len(match_seeds))

  return match_list, match_seeds

def basic_pass2(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    flag = Mydatabase.check(seed)
    if flag == "***" or flag == "friends_only":
      followers = update(flag, 'followers_only', seed)
    elif flag == "followers_only" or flag == "all":
      followers = Mydatabase.select("select userID from follow_graph where userID = \'" + seed + "\'")
      followers = tuple2list(followers)
    else: continue

    match_list = list(set(match_list) | set(followers))
    match_seeds = match(seed, followers, match_seeds)

  return match_list, match_seeds


def basic_pass3(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    flag = Mydatabase.check(seed)
    if flag == "***" or flag == "followers_only":
      friends = update(flag, 'friends_only', seed)
    elif flag == "friends_only" or flag == "all":
      friends = Mydatabase.select("select followerID from follow_graph where userID = \'" + seed + "\'")
      friends = tuple2list(friends)
    else: continue

    for friend in friends:
      flag = Mydatabase.check(friend)
      if flag == "***" or flag == "friends_only":
        followers = update(flag, 'followers_only', friend)
      elif flag == "followers_only" or flag == "all":
        followers = Mydatabase.select("select userID from follow_graph where userID = \'" + friend + "\'")
        followers = tuple2list(followers)
      else: continue

      match_list = list(sert(match_list) | set(followers))
      match_seeds = match(seed, followers, match_seeds)

  return match_list, match_seeds



def basic_pass4(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    flag = Mydatabase.check(seed)
    if flag == "***" or flag == "friends_only":
      followers = update(flag, 'followers_only', seed)
    elif flag == "followers_only" or flag == "all":
      followers = Mydatabase.select("select userID from follow_graph where userID = \'" + seed + "\'")
      followers = tuple2list(followers)
    else: continue

    for follower in followers:
      flag = Mydatabase.check(follower)
      if flag == "***" or flag == "followers_only":
        friends = update(flag, 'friends_only', follower)
      elif flag == "friends_only" or flag == "all":
        friends = Mydatabase.select("select followerID from follow_graph where userID = \'" + follower + "\'")
        friends = tuple2list(friends)
      else: continue

      match_list = list(set(match_list) | set(friends))
      match_seeds = match(seed, friends, match_seeds)

  return match_list, match_seeds



def basic_pass5(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    flag = Mydatabase.check(seed)
    if flag == "***" or flag == "followers_only":
      friends = update(flag, 'friends_only', seed)
    elif flag == "friends_only" or flag == "all":
      friends = Mydatabase.select("select followerID from follow_graph where userID = \'" + seed + "\'")
      friends = tuple2list(friends)
    else: continue

    for friend in friends:
      flag = Mydatabase.check(friend)
      if flag == "***" or flag == "followers_only":
        friends_2 = update(flag, 'friends_only', friend)
      elif flag == "friends_only" or flag == "all":
        friends_2 = Mydatabase.select("select followerID from follow_graph where userID = \'" + friend + "\'")
        friends_2 = tuple2list(friends)
      else: continue

      match_list = list(set(match_list) | set(friends_2))
      match_seeds = match(seed, friends_2, match_seeds)


  return match_list, match_seeds


def basic_pass6(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    flag = Mydatabase.check(seed)
    if flag == "***" or flag == "friends_only":
      followers = update(flag, 'followers_only', seed)
    elif flag == "followers_only" or flag == "all":
      followers = Mydatabase.select("select userID from follow_graph where userID = \'" + seed + "\'")
      followers = tuple2list(followers)
    else: continue

    for follower in followers:
      flag = Mydatabase.check(follower)
      if flag == "***" or flag == "friends_only":
        followers_2 = update(flag, 'followers_only', follower)
      elif flag == "followers_only" or flag == "all":
        followers_2 = Mydatabase.select("select userID from follow_graph where userID = \'" + follower + "\'")
        followers_2 = tuple2list(followers_2)
      else: continue

      match_list = list(set(match_list) | set(followers_2))
      match_seeds = match(seed, followers_2, match_seeds)


  return match_list, match_seeds


def join_dic(dics):
  ans = {}
  for dic in dics:
    for k, v in dic.items():
      if k not in ans: ans[k] = v
      else: ans[k] = ans[k] + v

  for k, v in ans.items():
    s = set()
    temp = [x for x in v if x in s or s.add(x)]
    ans[k] = list(set(temp))

  return ans
