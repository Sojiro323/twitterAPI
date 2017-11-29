#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mymodule import Mail
from mymodule import MytwitterAPI
from mymodule import Mypickle
from mymodule import Mydatabase
import json
import os
import sys


path = "./pickle/"

'''
load_files = Mypickle.load(path, ['check_list','friends_doneID','followers_doneID'])
check_list = load_files[0]
friends_doneID = load_files[1]
followers_doneID = load_files[2]

print(len(check_list),len(friends_doneID),len(followers_doneID))


users_list = MytwitterAPI.join_params(check_list.keys(), count = 100)
Mypickle.save(path, users_list)
'''


load_files = Mypickle.load(path, ['users_list','friends_doneID','followers_doneID'])
user_list = load_files[0]
friends_doneID = load_files[1]
followers_doneID = load_files[2]

print(len(user_list),len(friends_doneID),len(followers_doneID))


def check_status(userID, key):
    if userID in friends_doneID and userID in followers_doneID: return "all"
    elif userID in friends_doneID: return "friends_only"
    elif userID in followers_doneID: return "followers_only"
    elif key: return "protected"
    else: return "***"


for i, users in enumerate(user_list):

    responce = MytwitterAPI.lookup(users)

    if responce.status_code != 200:
        print("Error code: %d" %(responce.status_code))
        sys.exit()

    limit = int(responce.headers['x-rate-limit-remaining']) if 'x-rate-limit-remaining' in responce.headers else 0
    if limit == 0:time.sleep(900)

    ress = json.loads(responce.text)
    for res in ress:
        state = check_status(res["id_str"], res["protected"])
        Mydatabase.insert("checked_list", (res["id_str"], state, res["lang"], res["friends_count"], res["followers_count"]))

    if i+1 < len(users_list):
        users_list = user_list[i+1:]
        Mypickle.save(path, users_list)
