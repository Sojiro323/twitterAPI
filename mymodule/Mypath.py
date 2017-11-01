from mymodule import Mypickle

path_pattern = ["1","2","3","4","5","6","mutual"]

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

  if pattern is path_pattern[6]:#mutual

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
