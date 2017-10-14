#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mymodule import Mail
from mymodule import MytwitterAPI
from mymodule import Mypickle
import time
import json
import os
import sys

'''global variable'''
parh = "./pickle/"



def recommendation(userID):

    if os.path.exists(path + "path_score.pickle"): path_score = Mypickle.load(path,"path_score") #key : path_index
    else: path_score = {0:0.33, 1:0.33, 2:0.33}#friends_sougo,friends-friends.,followers-followers
    sorted(path_score.items(), key = lambda x:x[1])

    show_user = []

    for key , value in path_score.items():
        predict_node = follow_the_path(userID, path_score, key)
        show_user.append(predict_node)

    show_user = node_sort(show_user, path_score)
    discovered_seeds, p_check = personal_check(show_user)
    path_score = update_score(path_score, p_check)
    Mypickle.save('./pickle', path_score)

    return discovered_seeds


def follow_the_path(userID, path_score, key):

    load_files = Mypickle.load(path, ['friends_dic','followers_dic'])
    friends_dic = load_files[0]
    followers_dic = load_files[1]

    match = []

    if key is 0:
        friends = MytwitterAPI.get_node(userID, friends_dic)
        followers = MytwitterAPI.get_node(userID, followers_dic)
        match = list(set(friends) & set(followers))
    elif key is 1:
        friends = MytwitterAPI.get_node(userID,friends_dic)
        for friend in friends:
            match = match + MytwitterAPI.get_node(friend,friends_dic)
            #match = list(set(match))
    elif key is 2:
        followers = MytwitterAPI.get_node(userID,followers_dic)
        for follower in followers:
            match = match + MytwitterAPI.get_node(follower,followers_dic)
            #match = list(set(match))
    else:
        print("key is not exist")

    return match


def node_sort(show_user, path_score):

    return show_user



def personal_check(show_user):

    discovered_seeds = []
    p_check = []

    return discovered_seeds, p_check


def updata_score(path_score, p_check):

    return path_score

def visualize(answer_list):

    print("visualize")


### Execute
if __name__ == "__main__":

    seeds = ["2294473200"]
    get_num = 10

    answer_list = []

    while(len(answer_list) < get_num):
        userID = seeds.pop(0)
        discovered_seeds = recommendation(userID)
        answer_list = answer_list + discovered_seeds
        seeds = seeds + discovered_seeds

    visualize(answer_list)
