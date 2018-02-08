from connect import database

path_pattern = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39"]

def get_match(pattern, seeds):

  if pattern is path_pattern[0]:#friend
    match_list, match_seeds = basic_pass1(seeds)

  elif pattern is path_pattern[1]:#follower
    match_list, match_seeds = basic_pass2(seeds)

  elif pattern is path_pattern[2]:#com_friend
    match_list, match_seeds = basic_pass3(seeds)

  elif pattern is path_pattern[3]:#com_follower
    match_list, match_seeds = basic_pass4(seeds)

  elif pattern is path_pattern[4]:#friend_friend
    match_list, match_seeds = basic_pass5(seeds)

  elif pattern is path_pattern[5]:#follower_follower
    match_list, match_seeds = basic_pass6(seeds)

  elif pattern is path_pattern[6]:#mutual
    match_list, match_seeds = basic_pass7(seeds)

  elif pattern is path_pattern[7]:#8
    match_list, match_seeds = basic_pass8(seeds)

  elif pattern is path_pattern[8]:#9
    match_list, match_seeds = basic_pass9(seeds)

  elif pattern is path_pattern[9]:#10
    match_list, match_seeds = basic_pass10(seeds)

  elif pattern is path_pattern[10]:#11
    match_list, match_seeds = basic_pass11(seeds)

  elif pattern is path_pattern[11]:#12
    match_list, match_seeds = basic_pass12(seeds)

  elif pattern is path_pattern[12]:#13
    match_list, match_seeds = basic_pass13(seeds)

  elif pattern is path_pattern[13]:#14
    match_list, match_seeds = basic_pass14(seeds)

  elif pattern is path_pattern[14]:#15
    match_list, match_seeds = basic_pass15(seeds)

  elif pattern is path_pattern[15]:#16
    match_list, match_seeds = basic_pass16(seeds)

  elif pattern is path_pattern[16]:#17
    match_list, match_seeds = basic_pass17(seeds)

  elif pattern is path_pattern[17]:#18
    match_list, match_seeds = basic_pass18(seeds)

  elif pattern is path_pattern[18]:#19
    match_list, match_seeds = basic_pass19(seeds)

  elif pattern is path_pattern[19]:#20
    match_list, match_seeds = basic_pass20(seeds)

  elif pattern is path_pattern[20]:#21
    match_list, match_seeds = basic_pass21(seeds)

  elif pattern is path_pattern[21]:#22
    match_list, match_seeds = basic_pass22(seeds)

  elif pattern is path_pattern[22]:#23
    match_list, match_seeds = basic_pass23(seeds)

  elif pattern is path_pattern[23]:#24
    match_list, match_seeds = basic_pass24(seeds)

  elif pattern is path_pattern[24]:#25
    match_list, match_seeds = basic_pass25(seeds)

  elif pattern is path_pattern[25]:#26
    match_list, match_seeds = basic_pass26(seeds)

  elif pattern is path_pattern[26]:#27
    match_list, match_seeds = basic_pass27(seeds)

  elif pattern is path_pattern[27]:#28
    match_list, match_seeds = basic_pass28(seeds)

  elif pattern is path_pattern[28]:#29
    match_list, match_seeds = basic_pass29(seeds)

  elif pattern is path_pattern[29]:#30
    match_list, match_seeds = basic_pass30(seeds)

  elif pattern is path_pattern[30]:#31
    match_list, match_seeds = basic_pass31(seeds)

  elif pattern is path_pattern[31]:#32
    match_list, match_seeds = basic_pass32(seeds)

  elif pattern is path_pattern[32]:#33
    match_list, match_seeds = basic_pass33(seeds)

  elif pattern is path_pattern[33]:#34
    match_list, match_seeds = basic_pass34(seeds)

  elif pattern is path_pattern[34]:#35
    match_list, match_seeds = basic_pass35(seeds)
    match_seeds = join_dic([match_seeds])

  elif pattern is path_pattern[35]:#36
    match_list, match_seeds = basic_pass36(seeds)

  elif pattern is path_pattern[36]:#37
    match_list, match_seeds = basic_pass37(seeds)

  elif pattern is path_pattern[37]:#38
    match_list, match_seeds = basic_pass38(seeds)

  elif pattern is path_pattern[38]:#39
    match_list, match_seeds = basic_pass39(seeds)

  else:
    print("key error : {0}".format(pattern))

  return match_list, match_seeds

def match(seed, match_list, match_seeds):

  if len(match_list) == 0:
    return match_seeds

  for match in match_list:
    if match not in match_seeds: match_seeds[match] = []
    match_seeds[match].append(seed)

  return match_seeds

def update(goal, userID):

  friends = []
  followers = []

  if goal == "friends_only":
    friends = database.select('select followerID from follow_graph where userID = \'' + userID + '\'')
    friends = tuple2list(friends)
    return friends
  elif goal == "followers_only":
    followers = database.select('select userID from follow_graph where followerID = \'' + userID + '\'')
    followers = tuple2list(followers)
    return followers
  else:
    friends = database.select('select followerID from follow_graph where userID = \'' + userID + '\'')
    friends = tuple2list(friends)
    followers = database.select('select userID from follow_graph where followerID = \'' + userID + '\'')
    followers = tuple2list(followers)
    return friends, followers



def tuple2list(tp):
  ans = []
  for t in tp:
    ans.append(t[0])
  return ans



def basic_pass1(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends = update("friends_only",seed)
    if len(friends) == 0: continue

    friends = list(set(friends) - set(seeds))
    match_list = list(set(match_list) | set(friends))
    match_seeds = match(seed, friends, match_seeds)

  return match_list, match_seeds

def basic_pass2(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    followers = update("followers_only",seed)
    if len(followers) == 0: continue

    followers = list(set(followers) - set(seeds))
    match_list = list(set(match_list) | set(followers))
    match_seeds = match(seed, followers, match_seeds)

  return match_list, match_seeds


def basic_pass3(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends = update("friends_only",seed)
    if len(friends) == 0: continue

    for friend in friends:
      followers = update("followers_only",friend)
      if len(followers) == 0: continue

      followers = list(set(followers) - set(seeds))
      match_list = list(set(match_list) | set(followers))
      match_seeds = match(seed, followers, match_seeds)

  return match_list, match_seeds



def basic_pass4(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    followers = update("followers_only",seed)
    if len(followers) == 0: continue

    for follower in followers:
      friends = update("friends_only",follower)
      if len(friends) == 0: continue

      friends = list(set(friends) - set(seeds))
      match_list = list(set(match_list) | set(friends))
      match_seeds = match(seed, friends, match_seeds)

  return match_list, match_seeds



def basic_pass5(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends = update("friends_only",seed)
    if len(friends) == 0: continue

    for friend in friends:
      friends_2 = update("friends_only",friend)
      if len(friends_2) == 0: continue

      friends_2 = list(set(friends_2) - set(seeds))
      match_list = list(set(match_list) | set(friends_2))
      match_seeds = match(seed, friends_2, match_seeds)


  return match_list, match_seeds


def basic_pass6(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    followers = update("followers_only",seed)
    if len(followers) == 0: continue

    for follower in followers:
      followers = update("followers_only",follower)
      if len(followers_2) == 0: continue

      followers_2 = list(set(followers_2) - set(seeds))
      match_list = list(set(match_list) | set(followers_2))
      match_seeds = match(seed, followers_2, match_seeds)


  return match_list, match_seeds

def basic_pass7(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    ans = list(set(followers) & set(friends))
    ans = list(set(ans) - set(seeds))
    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass8(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for friend in friends:
      friends2followers = update("followers_only",friend)
      if len(friends2followers) == 0: continue

      ans = list(set(followers) & set(friends2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass9(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends = update("friends_only", seed)
    if len(friends) == 0: continue

    for friend in friends:
      friends2followers = update("followers_only",friend)
      if len(friends2followers) == 0: continue

      ans = list(set(friends) & set(friends2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass10(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends = update("friends_only", seed)
    if len(friends) == 0: continue

    for friend in friends:
      friends2friends, friends2followers = update("all",friend)
      if len(friends2followers) == 0 or len(friends2friends) == 0: continue

      ans = list(set(friends2friends) & set(friends2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass11(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual: ans = update("followers_only", m)

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass12(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    followers = update("followers_only", seed)
    if len(followers) == 0: continue

    for follower in followers:
      followers2friends = update("friends_only",follower)
      if len(followers2friends) == 0: continue

      ans = list(set(followers) & set(followers2friends))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass13(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for follower in followers:
      followers2friends = update("friends_only",follower)
      if len(followers2friends) == 0: continue

      ans = list(set(friends) & set(followers2friends))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass14(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual: ans = update("friends_only", m)

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass15(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    followers = update("followers_only", seed)
    if len(followers) == 0: continue

    for follower in followers:
      followers2friends, followers2followers = update("all",follower)
      if len(followers2followers) == 0 or len(followers2friends) == 0: continue

      ans = list(set(followers2friends) & set(followers2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass16(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for friend in friends:
      friends2friends = update("friends_only",friend)
      if len(friends2friends) == 0: continue

      ans = list(set(followers) & set(friends2friends))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass17(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends = update("friends_only", seed)
    if len(friends) == 0: continue

    for friend in friends:
      friends2friends = update("friends_only",friend)
      if len(friends2friends) == 0: continue

      ans = list(set(friends) & set(friends2friends))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass18(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    followers = update("followers_only", seed)
    if len(followers) == 0: continue

    for follower in followers:
      followers2followers = update("followers_only",follower)
      if len(followers2followers) == 0: continue

      ans = list(set(followers) & set(followers2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass19(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for follower in followers:
      followers2followers = update("followers_only",follower)
      if len(follower2followers) == 0: continue

      ans = list(set(friends) & set(followers2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass20(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for friend in friends:
      friends2followers = update("followers_only",friend)
      if len(friends2followers) == 0: continue

      ans = list(set(followers) & set(friend) & set(friends2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass21(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for follower in followers:
      followers2friends = update("friends_only",follower)
      if len(follower2friends) == 0: continue

      ans = list(set(friends) & set(followers) & set(followers2friends))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass22(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for friend in friends:
      friends2friends = update("friends_only",friend)
      if len(friends2friends) == 0: continue

      ans = list(set(followers) & set(friends) & set(friends2friends))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass23(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for follower in followers:
      followers2followers = update("followers_only",follower)
      if len(follower2followers) == 0: continue

      ans = list(set(friends) & set(followers) & set(followers2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass24(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual:
      mutual2friends, mutual2followers = update("all", m)

      ans = list(set(mutual2friends) & set(mutual2followers))
      ans = list(set(ans) - set(seeds))

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass25(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for friend in friends:
      friends2friends, friends2followers = update("all",friend)
      if len(friends2followers) == 0 or len(friends2friends): continue

      ans = list(set(followers) & set(friends2followers) & set(friends2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass26(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends = update("friends_only", seed)
    if len(friends) == 0: continue

    for friend in friends:
      friends2friends, friends2followers = update("all",friend)
      if len(friends2friends) == 0 or len(friends2followers): continue

      ans = list(set(friends) & set(friends2friends) & set(friends2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass27(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual:
      mutual2followers = update("followers_only", m)

      ans = list(set(mutual2followers) & set(followers))
      ans = list(set(ans) - set(seeds))

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass28(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual:
      mutual2followers = update("followers_only", m)

      ans = list(set(mutual2followers) & set(friends))
      ans = list(set(ans) - set(seeds))

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass29(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual:
      mutual2friends = update("friends_only", m)

      ans = list(set(mutual2friends) & set(followers))
      ans = list(set(ans) - set(seeds))

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

  def basic_pass30(seeds):

    match_list = []
    match_seeds = {}

    for seed in seeds:
      friends, followers = update("all",seed)
      if len(friends) == 0 or len(followers) == 0: continue

      mutual = list(set(followers) & set(friends))
      mutual = list(set(mutual) - set(seeds))

      for m in mutual:
        mutual2friends = update("friends_only", m)

        ans = list(set(mutual2friends) & set(friends))
        ans = list(set(ans) - set(seeds))

      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

    return match_list, match_seeds

def basic_pass31(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    followers = update("followers_only", seed)
    if len(followers) == 0: continue

    for follower in followers:
      followers2friends, followers2followers = update("all",follower)
      if len(followers2followers) == 0 or len(followers2friends) == 0: continue

      ans = list(set(followers2friends) & set(followers2followers) & set(followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass32(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all", seed)
    if len(followers) == 0: continue

    for follower in followers:
      followers2friends, followers2followers = update("all",follower)
      if len(followers2followers) == 0 or len(followers2friends) == 0: continue

      ans = list(set(followers2friends) & set(followers2followers) & set(friends))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass33(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers  = update("all", seed)
    if len(friends) == 0 or len(followers) == 0: continue

    for friend in friends:
      friends2friends, friends2followers = update("all",friend)
      if len(friends2followers) == 0 or len(friends2friends): continue

      ans = list(set(followers) & set(friends) & set(friends2followers) & set(friends2followers))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass34(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual:
      mutual2followers = update("followers_only", m)

      ans = list(set(mutual2followers) & set(mutual))
      ans = list(set(ans) - set(seeds))

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass35(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual:
      mutual2friends = update("friends_only", m)

      ans = list(set(mutual2friends) & set(mutual))
      ans = list(set(ans) - set(seeds))

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass36(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    followers = update("followers_only", seed)
    if len(followers) == 0: continue

    for follower in followers:
      followers2friends, followers2followers = update("all",follower)
      if len(followers2followers) == 0 or len(followers2friends) == 0: continue

      ans = list(set(followers2friends) & set(followers2followers) & set(followers) & set(friends))
      ans = list(set(ans) - set(seeds))
      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def basic_pass37(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual:
      mutual2friends, mutual2followers = update("all", m)

      ans = list(set(mutual2friends) & set(mutual2followers) & set(followers))
      ans = list(set(ans) - set(seeds))

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

  def basic_pass38(seeds):

    match_list = []
    match_seeds = {}

    for seed in seeds:
      friends, followers = update("all",seed)
      if len(friends) == 0 or len(followers) == 0: continue

      mutual = list(set(followers) & set(friends))
      mutual = list(set(mutual) - set(seeds))

      for m in mutual:
        mutual2friends, mutual2followers = update("all", m)

        ans = list(set(mutual2friends) & set(mutual2followers) & set(friends))
        ans = list(set(ans) - set(seeds))

      match_list = list(set(match_list) | set(ans))
      match_seeds = match(seed, ans, match_seeds)

    return match_list, match_seeds

def basic_pass39(seeds):

  match_list = []
  match_seeds = {}

  for seed in seeds:
    friends, followers = update("all",seed)
    if len(friends) == 0 or len(followers) == 0: continue

    mutual = list(set(followers) & set(friends))
    mutual = list(set(mutual) - set(seeds))

    for m in mutual:
      mutual2friends, mutual2followers = update("all", m)

      ans = list(set(mutual2friends) & set(mutual2followers) & set(mutual))
      ans = list(set(ans) - set(seeds))

    match_list = list(set(match_list) | set(ans))
    match_seeds = match(seed, ans, match_seeds)

  return match_list, match_seeds

def join_dic(dics):
  ans = {}
  for dic in dics:
    for k, v in dic.items():
      if k not in ans: ans[k] = v
      else: ans[k] = ans[k] + v

  for k, v in ans.items():
    """s = set()
    temp = [x for x in v if x in s or s.add(x)]
    ans[k] = list(set(temp))"""
    ans[k] = list(set(v))

  return ans
