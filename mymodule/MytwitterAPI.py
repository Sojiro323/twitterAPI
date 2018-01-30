from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError
from mymodule import Mypickle
import yaml

### Constants


def create_oath_session(oath_key_dict):

    f = open('../password/twitterAPI.yml', 'r+')
    oath_key_dict = yaml.load(f)

    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )

    return oath

def show(user_ID):

    url = "https://api.twitter.com/1.1/users/show.json?"
    params = {
        "user_id": user_ID
        }
    oath = create_oath_session(oath_key_dict)
    try:
        responce = oath.get(url, params = params)
    except ConnectionError as e:
        return show(user_ID)
    return responce


def lookup(users_ID):
    url = "https://api.twitter.com/1.1/users/lookup.json?"
    params = {
        "user_id": users_ID,
        "stringify_ids": "true"
        }
    oath = create_oath_session(oath_key_dict)
    try:
        responce = oath.post(url, params = params)
    except ConnectionError as e:
        return lookup(users_ID)
    return responce



def followers(userID):

    url = "https://api.twitter.com/1.1/followers/ids.json?"
    params = {
        "user_id": userID,
        "stringify_ids": "true"
        }
    oath = create_oath_session(oath_key_dict)
    try:
        responce = oath.get(url, params = params)
        #responce = oath.post(url, params = params)
    except ConnectionError as e:
        return followers(userID)
    return responce


def friends(userID):
    url = "https://api.twitter.com/1.1/friends/ids.json?"
    params = {
        "user_id": userID,
        "stringify_ids": "true"
        }
    oath = create_oath_session(oath_key_dict)
    try:
        responce = oath.get(url, params = params)
        #responce = oath.post(url, params = params)
    except ConnectionError as e:
        return friends(userID)
    return responce


def join_params(params_list,*,count = 0):

    lookup = ""

    if count == 0:
        for param in params_list:
            lookup = lookup + "," + param
        lookup = lookup[1:]
        return lookup


    counts = [0,0]
    return_list = []

    for param in params_list:
        lookup = lookup + "," + param
        counts[0]+= 1
        if counts[0] == count:
            lookup = lookup[1:]
            return_list.append(lookup)
            counts[0] = 0
            counts[1]+= 1
            lookup = ""

    if len(params_list) < count: return [lookup]
    if return_list[-1] == "": return_list.pop()

    return return_list
