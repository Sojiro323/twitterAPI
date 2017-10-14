from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError
from mymodule import Mypickle

### Constants
oath_key_dict = {
    "consumer_key": "r3KRXHuwQVJ0wB9GI75XMGYOn",
    "consumer_secret": "f73EwbM5SR56aNbcWK4gVlSnnutS1zTrrVcVVL5MdLh6EDtmeo",
    "access_token": "1307786538-ZvscWGeSot5JU0yIpPb1OXL2buysCsOTa2MvAdA",
    "access_token_secret": "zupEdxQ6Gulfwxu5n0UZWSYqj805R8DqEjeU9KVFbjbaG"
}

def create_oath_session(oath_key_dict):

    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )

    return oath

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
