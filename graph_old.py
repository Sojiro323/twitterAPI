from connect import database
from mymodule import Myyaml



def get_match(pattern, seeds):

  from mymodule import Myyaml
  path_pattern = Myyaml.load("path")["path_com"]["39"]

  if pattern == path_pattern[0]:#friend
    match_list, match_seeds = basic_pass1(seeds)

  elif pattern == path_pattern[1]:#follower
    match_list, match_seeds = basic_pass2(seeds)

  elif pattern == path_pattern[2]:#com_friend
    match_list, match_seeds = basic_pass3(seeds)

  elif pattern == path_pattern[3]:#com_follower
    match_list, match_seeds = basic_pass4(seeds)

  elif pattern == path_pattern[4]:#friend_friend
    match_list, match_seeds = basic_pass5(seeds)

  elif pattern == path_pattern[5]:#follower_follower
    match_list, match_seeds = basic_pass6(seeds)

  elif pattern == path_pattern[6]:#mutual
    match_list, match_seeds = basic_pass7(seeds)

  elif pattern == path_pattern[7]:#8
    match_list, match_seeds = basic_pass8(seeds)

  elif pattern == path_pattern[8]:#9
    match_list, match_seeds = basic_pass9(seeds)

  elif pattern == path_pattern[9]:#10
    match_list, match_seeds = basic_pass10(seeds)

  elif pattern == path_pattern[10]:#11
    match_list, match_seeds = basic_pass11(seeds)

  elif pattern == path_pattern[11]:#12
    match_list, match_seeds = basic_pass12(seeds)

  elif pattern == path_pattern[12]:#13
    match_list, match_seeds = basic_pass13(seeds)

  elif pattern == path_pattern[13]:#14
    match_list, match_seeds = basic_pass14(seeds)

  elif pattern == path_pattern[14]:#15
    match_list, match_seeds = basic_pass15(seeds)

  elif pattern == path_pattern[15]:#16
    match_list, match_seeds = basic_pass16(seeds)

  elif pattern == path_pattern[16]:#17
    match_list, match_seeds = basic_pass17(seeds)

  elif pattern == path_pattern[17]:#18
    match_list, match_seeds = basic_pass18(seeds)

  elif pattern == path_pattern[18]:#19
    match_list, match_seeds = basic_pass19(seeds)

  elif pattern == path_pattern[19]:#20
    match_list, match_seeds = basic_pass20(seeds)

  elif pattern == path_pattern[20]:#21
    match_list, match_seeds = basic_pass21(seeds)

  elif pattern == path_pattern[21]:#22
    match_list, match_seeds = basic_pass22(seeds)

  elif pattern == path_pattern[22]:#23
    match_list, match_seeds = basic_pass23(seeds)

  elif pattern == path_pattern[23]:#24
    match_list, match_seeds = basic_pass24(seeds)

  elif pattern == path_pattern[24]:#25
    match_list, match_seeds = basic_pass25(seeds)

  elif pattern == path_pattern[25]:#26
    match_list, match_seeds = basic_pass26(seeds)

  elif pattern == path_pattern[26]:#27
    match_list, match_seeds = basic_pass27(seeds)

  elif pattern == path_pattern[27]:#28
    match_list, match_seeds = basic_pass28(seeds)

  elif pattern == path_pattern[28]:#29
    match_list, match_seeds = basic_pass29(seeds)

  elif pattern == path_pattern[29]:#30
    match_list, match_seeds = basic_pass30(seeds)

  elif pattern == path_pattern[30]:#31
    match_list, match_seeds = basic_pass31(seeds)

  elif pattern == path_pattern[31]:#32
    match_list, match_seeds = basic_pass32(seeds)

  elif pattern == path_pattern[32]:#33
    match_list, match_seeds = basic_pass33(seeds)

  elif pattern == path_pattern[33]:#34
    match_list, match_seeds = basic_pass34(seeds)

  elif pattern == path_pattern[34]:#35
    match_list, match_seeds = basic_pass35(seeds)
    match_seeds = join_dic([match_seeds])

  elif pattern == path_pattern[35]:#36
    match_list, match_seeds = basic_pass36(seeds)

  elif pattern == path_pattern[36]:#37
    match_list, match_seeds = basic_pass37(seeds)

  elif pattern == path_pattern[37]:#38
    match_list, match_seeds = basic_pass38(seeds)

  elif pattern == path_pattern[38]:#39
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
  return [t[0] in t in tp]



def basic_pass1(seed):

  match_list = []

  friends = update("friends_only",seed, seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'): Mypickle.save(DIR, friends, seed + '_1')

  return friends

def basic_pass2(seed):

  match_list = []

  followers = update("followers_only",seed, seed)
  if not os.path.isfile(DIR + seed + '_2.pickle'): Mypickle.save(DIR, followers, seed + '_2')

  return followers


def basic_pass3(seed):

  match_list = []

  friends = update("friends_only",seed ,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')

  for friend in friends:
    followers = update("followers_only",friend, seed)
    match_list = list(set(match_list) | set(followers))

  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, match_list, seed + '_3')
  return match_list



def basic_pass4(seed):

  match_list = []


  followers = update("followers_only",seed, seed)
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    friends = update("friends_only",follower, seed)
    match_list = list(set(match_list) | set(friends))

  if not os.path.isfile(DIR + seed + '_4.pickle'):  Mypickle.save(DIR, match_list, seed + '_4')
  return match_list



def basic_pass5(seed):

  match_list = []


  friends = update("friends_only",seed, seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')

  for friend in friends:
    friends_2 = update("friends_only",friend,seed)
    match_list = list(set(match_list) | set(friends_2))

  if not os.path.isfile(DIR + seed + '_5.pickle'):  Mypickle.save(DIR, match_list, seed + '_5')
  return match_list


def basic_pass6(seed):

  match_list = []


  followers = update("followers_only",seed,seed)
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers = update("followers_only",follower,seed)
    match_list = list(set(match_list) | set(followers_2))


  if not os.path.isfile(DIR + seed + '_6.pickle'):  Mypickle.save(DIR, match_list, seed + '_6')
  return match_list

def basic_pass7(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')
  match_list = list(set(followers) & set(friends))

  return match_list

def basic_pass8(seed):

  match_list = []
  frfo = []


  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for friend in friends:
    friends2followers = update("followers_only",friend,seed)
    frfo = list(set(friends2followers) & set(frfo))
    ans = list(set(followers) & set(friends2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, frfo, seed + '_3')
  return match_list

def basic_pass9(seed):

  match_list = []
  frfo = []

  friends = update("friends_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')

  for friend in friends:
    friends2followers = update("followers_only",friend,seed)
    frfo = list(set(friends2followers) & set(frfo))
    ans = list(set(friends) & set(friends2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, frfo, seed + '_3')
  return match_list

def basic_pass10(seed):

  match_list = []
  frfr = []
  frfo = []

  friends = update("friends_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')

  for friend in friends:
    friends2friends, friends2followers = update("all",friend,seed)
    frfo = list(set(friends2followers) & set(frfo))
    frfr = list(set(friends2friends) & set(frfr))
    ans = list(set(friends2friends) & set(friends2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_5.pickle'):  Mypickle.save(DIR, frfr, seed + '_5')
  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, frfo, seed + '_3')
  return match_list

def basic_pass11(seed):

  match_list = []

  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))
  mutual = list(set(mutual) - set(seeds))

  for m in mutual: ans = update("followers_only", m,seed)

  match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass12(seed):

  match_list = []
  fofr = []

  followers = update("followers_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2friends = update("friends_only",follower,seed)
    fofr = list(set(followers2friends) & set(fofr))
    ans = list(set(followers) & set(followers2friends))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_4.pickle'):  Mypickle.save(DIR, fofr, seed + '_4')
  return match_list

def basic_pass13(seed):

  match_list = []
  fofr = []

  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2friends = update("friends_only",follower,seed)
    fofr = list(set(followers2friends) & set(fofr))
    ans = list(set(friends) & set(followers2friends))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_4.pickle'):  Mypickle.save(DIR, fofr, seed + '_4')
  return match_list

def basic_pass14(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))
  mutual = list(set(mutual) - set(seeds))

  for m in mutual: ans = update("friends_only", m,seed)

  match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass15(seed):

  match_list = []
  fofo = []
  fofr = []

  followers = update("followers_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, followers, seed + '_1')

  for follower in followers:
    followers2friends, followers2followers = update("all",follower,seed)
    fofr = list(set(followers2friends) & set(fofr))
    fofo = list(set(followers2followers) & set(fofo))
    ans = list(set(followers2friends) & set(followers2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_4.pickle'):  Mypickle.save(DIR, fofr, seed + '_4')
  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, fofo, seed + '_3')
  return match_list

def basic_pass16(seed):

  match_list = []
  frfr = []

  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for friend in friends:
    friends2friends = update("friends_only",friend,seed)
    frfr = list(set(friends2friends) & set(frfr))
    ans = list(set(followers) & set(friends2friends))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_5.pickle'):  Mypickle.save(DIR, frfr, seed + '_5')
  return match_list

def basic_pass17(seed):

  match_list = []
  frfr = []

  friends = update("friends_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')

  for friend in friends:
    friends2friends = update("friends_only",friend,seed)
    frfr = list(set(friends2friends) & set(frfr))
    ans = list(set(friends) & set(friends2friends))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_5.pickle'):  Mypickle.save(DIR, frfr, seed + '_5')
  return match_list

def basic_pass18(seed):

  match_list = []
  fofo = []

  followers = update("followers_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2followers = update("followers_only",follower,seed)
    fofo = list(set(followers2followers) & set(fofo))
    ans = list(set(followers) & set(followers2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, fofo, seed + '_3')
  return match_list

def basic_pass19(seed):

  match_list = []
  fofo = []


  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2followers = update("followers_only",follower,seed)
    fofo = list(set(followers2followers) & set(fofo))
    ans = list(set(follower) & set(friends) & set(followers2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_6.pickle'):  Mypickle.save(DIR, fofo, seed + '_6')
  return match_list

def basic_pass20(seed):

  match_list = []
  frfo = []

  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for friend in friends:
    friends2followers = update("followers_only",friend,seed)
    frfo = list(set(friends2followers) & set(frfo))
    ans = list(set(followers) & set(friend) & set(friends2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, frfo, seed + '_3')
  return match_list

def basic_pass21(seed):

  match_list = []
  fofr = []

  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2friends = update("friends_only",follower,seed)
    fofr = list(set(followers2friends) & set(fofr))
    ans = list(set(friends) & set(followers) & set(followers2friends))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_4.pickle'):  Mypickle.save(DIR, fofr, seed + '_4')
  return match_list

def basic_pass22(seed):

  match_list = []
  frfr = []

  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for friend in friends:
    friends2friends = update("friends_only",friend,seed)
    frfr = list(set(friends2friends) & set(frfr))
    ans = list(set(followers) & set(friends) & set(friends2friends))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_5.pickle'):  Mypickle.save(DIR, frfr, seed + '_5')
  return match_list

def basic_pass23(seed):

  match_list = []
  fofo = []

  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2followers = update("followers_only",follower,seed)
    fofo = list(set(followers2followers) & set(fofo))
    ans = list(set(friends) & set(followers) & set(followers2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_6.pickle'):  Mypickle.save(DIR, fofo, seed + '_6')
  return match_list

def basic_pass24(seed):

  match_list = []

  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
    mutual2friends, mutual2followers = update("all", m,seed)

    ans = list(set(mutual2friends) & set(mutual2followers))

    match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass25(seed):

  match_list = []
  frfr = []
  frfo = []

  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'): Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for friend in friends:
    friends2friends, friends2followers = update("all",friend,seed)
    frfr = list(set(friends2friends) & set(frfr))
    frfo = list(set(friends2followers) & set(frfo))
    ans = list(set(followers) & set(friends2followers) & set(friends2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_5.pickle'):  Mypickle.save(DIR, frfr, seed + '_5')
  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, frfo, seed + '_3')
  return match_list

def basic_pass26(seed):

  match_list = []
  frfr = []
  frfo = []

  friends = update("friends_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')

  for friend in friends:
    friends2friends, friends2followers = update("all",friend,seed)
    frfr = list(set(friends2friends) & set(frfr))
    frfo = list(set(friends2followers) & set(frfo))
    ans = list(set(friends) & set(friends2friends) & set(friends2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_5.pickle'):  Mypickle.save(DIR, frfr, seed + '_5')
  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, frfo, seed + '_3')
  return match_list

def basic_pass27(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
    mutual2followers = update("followers_only", m,seed)

    ans = list(set(mutual2followers) & set(followers))

    match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass28(seeds):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
    mutual2followers = update("followers_only", m,seed)

    ans = list(set(mutual2followers) & set(friends))

    match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass29(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
    mutual2friends = update("friends_only", m,seed)

    ans = list(set(mutual2friends) & set(followers))

    match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass30(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
      mutual2friends = update("friends_only", m,seed)

      ans = list(set(mutual2friends) & set(friends))

      match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass31(seed):

  match_list = []
  fofr = []
  fofo = []

  followers = update("followers_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2friends, followers2followers = update("all",follower,seed)
    fofr = list(set(followers2friends) & set(fofr))
    fofo = list(set(followers2followers) & set(fofo))
    ans = list(set(followers2friends) & set(followers2followers) & set(followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_4.pickle'):  Mypickle.save(DIR, fofr, seed + '_4')
  if not os.path.isfile(DIR + seed + '_6.pickle'):  Mypickle.save(DIR, fofo, seed + '_6')
  return match_list

def basic_pass32(seed):

  match_list = []
  fofr = []
  fofo = []

  friends, followers = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2friends, followers2followers = update("all",follower,seed)
    fofr = list(set(followers2friends) & set(fofr))
    fofo = list(set(followers2followers) & set(fofo))
    ans = list(set(followers2friends) & set(followers2followers) & set(friends))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_4.pickle'):  Mypickle.save(DIR, fofr, seed + '_4')
  if not os.path.isfile(DIR + seed + '_6.pickle'):  Mypickle.save(DIR, fofo, seed + '_6')
  return match_list

def basic_pass33(seed):

  match_list = []
  frfr = []
  frfo = []

  friends, followers  = update("all", seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for friend in friends:
    friends2friends, friends2followers = update("all",friend,seed)
    frfr = list(set(friends2friends) & set(frfr))
    frfo = list(set(friends2followers) & set(frfo))
    ans = list(set(followers) & set(friends) & set(friends2followers) & set(friends2followers))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_5.pickle'):  Mypickle.save(DIR, frfr, seed + '_5')
  if not os.path.isfile(DIR + seed + '_3.pickle'):  Mypickle.save(DIR, frfo, seed + '_3')
  return match_list

def basic_pass34(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
    mutual2followers = update("followers_only", m,seed)

    ans = list(set(mutual2followers) & set(mutual))

    match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass35(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
    mutual2friends = update("friends_only", m,seed)

    ans = list(set(mutual2friends) & set(mutual))

    match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass36(seed):

  match_list = []
  fofo = []
  fofr = []

  followers = update("followers_only", seed,seed)
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  for follower in followers:
    followers2friends, followers2followers = update("all",follower,seed)
    fofr = list(set(followers2friends) & set(fofr))
    fofo = list(set(followers2followers) & set(fofo))
    ans = list(set(followers2friends) & set(followers2followers) & set(followers) & set(friends))
    match_list = list(set(match_list) | set(ans))

  if not os.path.isfile(DIR + seed + '_4.pickle'):  Mypickle.save(DIR, fofr, seed + '_4')
  if not os.path.isfile(DIR + seed + '_6.pickle'):  Mypickle.save(DIR, fofo, seed + '_6')
  return match_list

def basic_pass37(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
    mutual2friends, mutual2followers = update("all", m,seed)

    ans = list(set(mutual2friends) & set(mutual2followers) & set(followers))

    match_list = list(set(match_list) | set(ans))

  return match_list

def basic_pass38(seed):

    match_list = []


    friends, followers = update("all",seed,seed)
    if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
    if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

    mutual = list(set(followers) & set(friends))

    for m in mutual:
      mutual2friends, mutual2followers = update("all", m,seed)

      ans = list(set(mutual2friends) & set(mutual2followers) & set(friends))

      match_list = list(set(match_list) | set(ans))

    return match_list

def basic_pass39(seed):

  match_list = []


  friends, followers = update("all",seed,seed)
  if not os.path.isfile(DIR + seed + '_1.pickle'):  Mypickle.save(DIR, friends, seed + '_1')
  if not os.path.isfile(DIR + seed + '_2.pickle'):  Mypickle.save(DIR, followers, seed + '_2')

  mutual = list(set(followers) & set(friends))

  for m in mutual:
    mutual2friends, mutual2followers = update("all", m,seed)

    ans = list(set(mutual2friends) & set(mutual2followers) & set(mutual))

    match_list = list(set(match_list) | set(ans))

  return match_list


def join_dic(dics):
  ans = {}
  for dic in dics:
    for k, v in dic.items():
      if k not in ans: ans[k] = v
      else: ans[k] = ans[k] + v

  return {k:list(set(v)) for k,v in ans.items()}
