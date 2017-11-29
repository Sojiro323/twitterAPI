from mymodule import Mypickle
import sys

path_pattern = ["1","2","3","4","5","6","mutual","3_3a","3_3b","3_35","3_36","3_4a","3_4b","3_45","3_46","3_5a","3_5a","3_5b","3_6a","3_6b","4_123","4_124","4_125","4_126","4_3456","4_35a","4_35b","4_36a","4_36b","4_45a","4_45b","4_46a","4_46b","5_1235","5_1236","5_1245","5_1246","5_13456","5_23456","all"]


#path = sys.argv[1]
path = "./pickle/"
load_files = Mypickle.load(path, ['friends_dic','followers_dic'])
friends_dic = load_files[0]
followers_dic = load_files[1]

def get_match():




  if pattern is path_pattern[0]:#friend

    for seed in seeds:
      if seed not in friends_dic: continue
      temp = friends_dic[seed]
      match_list = list(set(match_list) & set(temp))
      match_seeds = match(seed, match_list, match_seeds)

  elif pattern is path_pattern[1]:#follower

    for seed in seeds:
      if seed not in followers_dic: continue
      temp = followers_dic[seed]
      match_list = list(set(match_list) & set(temp))
      match_seeds = match(seed, match_list, match_seeds)

  elif pattern is path_pattern[2]:#com_friend

    for seed in seeds:
      if seed not in friends_dic: continue
      friends = friends_dic[seed]
      for friend in friends:
        if friend not in followers_dic: continue
        temp = followers_dic[friend]
        match_list = list(sert(match_list) & set(temp))
        match_seeds = match(seed, match_list, match_seeds)

  elif pattern is path_pattern[3]:#com_follower

    for seed in seeds:
      if seed not in followers_dic: continue
      followers = followers_dic[seed]
      for follower in followers:
        if follower not in friends_dic: continue
        temp = friends_dic[follower]
        match_list = list(set(match_list) & set(temp))
        match_seeds = match(seed, match_list, match_seeds)


  elif pattern is path_pattern[4]:#friend_friend

    for seed in seeds:
      if seed not in friends_dic: continue
      friends = friends_dic[seed]
      for friend in friends:
        if friend not in friends_dic: continue
        temp = friends_dic[friend]
        match_list = list(set(match_list) & set(temp))
        match_seeds = match(seed, match_list, match_seeds)


  elif pattern is path_pattern[5]:#follower_follower

    for seed in seeds:
      if seed not in followers_dic: continue
      followers = followers_dic[seed]
      for follower in followers:
        if follower not in followers_dic: continue
        temp = followers_dic[follower]
        match_list = list(set(match_list) & set(temp))
        match_seeds = match(seed, match_list, match_seeds)

  elif pattern is path_pattern[6]:#mutual

    for seed in seeds:
      if seed not in friends_dic or seed not in followers_dic: continue
      friends = friends_dic[seed]
      followers = followers_dic[seed]
      temp = list(set(friends) & set(followers))
      match_list = list(set(match_list) | set(temp))
      match_seeds = match(seed, match_list, match_seeds)


  else:
    print("key is not exist")

  return match_list, match_seeds


def match(seed, match_list, match_seeds):

  for match in match_list:
    if match not in match_seeds: match_seeds[match] = [seed]
    else: match_seeds[match] = match_seeds[match].append(seed)

  return match_seeds
