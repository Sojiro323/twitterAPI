#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mymodule import Mail
from mymodule import MytwitterAPI
from mymodule import Mypickle
import time
import json
import os
import sys
import random


'''global variable'''
parh = "./pickle/"
start_score = 0.1
path_pattern = ["0","1","2"]
seeds = ["2294473200"]
get_num = 10



def recommendation(pattern, seeds, seeds_score):

    match_list, match_seeds = follow_the_path(pattern, seeds)
    match_list = ranking(pattern, match_list, match_seeds, seeds_score)
    match_users, next_pattern, seeds_score = personal_check(pattern, match_list, match_seeds ,seeds_score)
    seeds = seeds + match_users

    return next_pattern, seeds, seeds_score



def follow_the_path(pattern, seeds):

    load_files = Mypickle.load(path, ['friends_dic','followers_dic'])
    friends_dic = load_files[0]
    followers_dic = load_files[1]

    match_list = []
    match_seeds = {}

    if key is 0:

    elif key is 1:

    elif key is 2:

    else:
        print("key is not exist")

    return match_list, match_seeds


def ranking(pattern, match_list, match_seeds, seeds_score):

    return match_list



def personal_check(pattern, match_list, match_seeds ,seeds_score):
    match_users = []

    for
        seeds = match_seeds[user]
            if#合っていたら
            seeds_score = update_score(True, pattern, seeds, seeds_score)
            seeds_score = init_score(user, seeds_score)
            match_users.append(user)
            else:#外したら
            seeds_score = update_score(False, pattern, seeds, seeds_score)

        continue_flag, next_pattern = check_continue(pattern, seeds_score)
        if continue_flag: return match_users, next_pattern, seeds_score

    return match_users, next_pattern, seeds_score

def init_score(user, seeds_score):

    return seeds_score


def updata_score(flag, pattern, match_seeds, seeds_score):

    return seeds_score


def passcheck_continue(pattern, seeds_score):

    return  continue_flag, next_pattern

def visualize(answer_list):

    print("visualize")


### Execute
if __name__ == "__main__":

    seeds_list = seeds
    start_num = len(seeds_list)

    seeds_score = {}

    for seed in seeds_list:
      seed_score = {p:[start_score,0,0] for p in path_pattern}  #[precision, good, bad]
      seeds_score[seed] = seed_score

    next_pattern = random.choice(path_pattern)

    while(len(seeds_list) < get_num + start_num):
        next_pattern, seeds_list, seeds_score = recommendation(next_pattern, seeds_list, seeds_score)

    visualize(seeds_list[start_num:])
