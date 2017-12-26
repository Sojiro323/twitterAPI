#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mymodule import Mail
from mymodule import MytwitterAPI
from mymodule import Mypickle
import time
import json
import os
import sys


#followers
#friends

#load_pickle
#acsessAPI
#addpop (follower or frined) checkID
#update (follower or frined)
#save_pickle


'''global'''
seeds = ["2432059932"] #CIS
max_hop = 3
path = "./pickle/"
'''end global'''



### Functions
def main():
    limit = [15,15,900] #friends,followers,user_show

    #check init or restart
    if os.path.exists(path + "friends_pop.pickle"):
        friends_pop, friends_doneID, friends_dic, followers_pop, followers_doneID, followers_dic, check_list = load_pickle()
    else:
        friends_pop, followers_pop, friends_doneID, followers_doneID, check_list = init()
        friends_dic = {}
        followers_dic = {}


    while(len(friends_pop) > 0 or len(followers_pop) > 0):

        if (limit.count(0) == 2) or ((len(friends_pop) == 0) and (limit[1] == 0)) or ((len(followers_pop) == 0) and (limit[0] == 0)):
            limit = save_pickle(friends_pop, friends_doneID, friends_dic, followers_pop, followers_doneID, followers_dic, check_list)


        while(len(friends_pop) > 0):
            if limit[0] == 0: break

            userID = friends_pop.pop(0)
            print('\nfriends_pop:{0} (hop={1})'.format(userID[0], userID[1]))
            friends_list, limit[0] = acsessAPI(userID,"friends") #friends_list = [id,id,id,id...]
            friends_list, limit[2], check_list = check(friends_list, check_list) #params of followers_count,friends_count,lang are checked
            friends_pop, friends_doneID, friends_dic, followers_pop, followers_doneID = update(userID, friends_list, friends_doneID, friends_pop, friends_dic, followers_doneID, followers_pop)


        while(len(followers_pop) > 0):
            if limit[1] == 0: break

            userID = followers_pop.pop(0)
            print('\nfollowers_pop:{0} (hop={1})'.format(userID[0], userID[1]))
            followers_list, limit[1] = acsessAPI(userID, "followers")
            followers_list, limit[2], check_list = check(followers_list, check_list) #params of followers_count,friends_count,lang are checked
            followers_pop, followers_doneID, followers_dic, friends_pop, friends_doneID = update(userID, followers_list, followers_doneID, followers_pop, followers_dic, friends_doneID, friends_pop)



def load_pickle():

    files = ['friends_pop', 'friends_doneID', 'friends_dic', 'followers_pop', 'followers_doneID', 'followers_dic', 'check_list']
    load_files = Mypickle.load(path,files)

    return load_files[0], load_files[1], load_files[2], load_files[3], load_files[4], load_files[5], load_files[6]


def save_pickle(friends_pop, friends_doneID, friends_dic, followers_pop, followers_doneID, followers_dic, check_list):

    start = int(time.time())
    Mypickle.save(path,friends_pop, friends_doneID, friends_dic, followers_pop, followers_doneID, followers_dic, check_list)
    end = int(time.time())

    print("start sleep...")
    time.sleep(900 - (end-start))
    print("resume!!")
    return [15,15,900]


def init():

    print("start init")
    friends_pop = []
    followers_pop = []
    friends_doneID = []
    followers_doneID = []
    check_list = {}

    for seed in seeds:
        friends_pop.append([seed,0])
        followers_pop.append([seed,0])
        friends_doneID.append(seed)
        followers_doneID.append(seed)
        check_list[seed] = True

    return friends_pop, followers_pop, friends_doneID, followers_doneID, check_list



def acsessAPI(userID, api):#userID = [userID,hop]

    return_list = []

    if api == "followers":responce = MytwitterAPI.followers(userID[0])
    else:responce = MytwitterAPI.friends(userID[0])

    limit = int(responce.headers['x-rate-limit-remaining']) if 'x-rate-limit-remaining' in responce.headers else 0
    if responce.status_code != 200:
        if (responce.status_code == 401) or (responce.status_code == 404): return [], limit
        print("Error code: %d" %(responce.status_code))
        Mail.sendmail("Error code: %d" %(responce.status_code))
        sys.exit()

    IDs = json.loads(responce.text)
    for ID in IDs["ids"]:
        return_list.append(ID)

    print('acsessAPI:return_list[{0}], limit[{1}/15]'.format(len(return_list),limit))
    return return_list, limit



def check(main_list, check_list):
    limit = 900
    return_list = []
    users_list = []

    if len(main_list) == 0:
        return [], limit, check_list

    for user in main_list:
        if user in check_list:
            if check_list[user][0] == "ja": users_list.append(user)
        else: users_list.append(user)

    users_list = MytwitterAPI.join_params(users_list, count = 100)

    for users in users_list:

        responce = MytwitterAPI.lookup(users)

        if responce.status_code != 200:
            if (responce.status_code == 401) or (responce.status_code == 404): return [], limit-1, check_list
            print("Error code: %d" %(responce.status_code))
            Mail.sendmail("Error code: %d" %(responce.status_code))
            sys.exit()

        limit = int(responce.headers['x-rate-limit-remaining']) if 'x-rate-limit-remaining' in responce.headers else 0
        if limit == 0:time.sleep(900)

        ress = json.loads(responce.text)
        for res in ress:
            if res["lang"] == "ja":
                return_list.append(res["id_str"])
                check_list[res["id_str"]] = [res["lang"], res["friends_count"], res["followers_count"]]
            else:
                check_list[res["id_str"]] = [res["lang"], res["friends_count"], res["folowers_count"]]
    print('check:return_list[{0}], check_list[{1}], limit[{2}/900]'.format(len(return_list), len(check_list), limit))
    return return_list, limit, check_list



def update(userID,main_list,main_doneID,main_pop,main_dic,sub_doneID,sub_pop):
    if  len(main_list) == 0:
        main_doneID.append(userID)
        print("Unauthorized(401) or page not found(404)")
        return main_pop, main_doneID, main_dic, sub_pop, sub_doneID

    main_dic[userID[0]] = main_list
    hop = userID[1]+1

    print("complete!!")

    if hop == max_hop:return main_pop, main_doneID, main_dic, sub_pop, sub_doneID

    for user in main_list:
        if user not in main_doneID:
            main_pop.append([user,hop])
            main_doneID.append(user)
        if user not in sub_doneID:
            sub_pop.append([user,hop])
            sub_doneID.append(user)


    return main_pop, main_doneID, main_dic, sub_pop, sub_doneID


### Execute
if __name__ == "__main__":
    main()
