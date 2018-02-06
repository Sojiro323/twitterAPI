from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError
from mymodule import Mypickle
from mymodule import Server_Mydatabase
import yaml
import time
import time from sleep

### Constants


def create_oath_session():

    ID = limit_check(api_name)

    f = open('../password/twitterAPI/' + str(ID) + '.yml', 'r+')
    oath_key_dict = yaml.load(f)
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )

    return oath, ID

def show(user_ID):

    url = "https://api.twitter.com/1.1/users/show.json?"
    params = {
        "user_id": user_ID
        }
    oath, ID = create_oath_session("show")
    try:
        responce = oath.get(url, params = params)
        insert2database(ID, responce)
    except ConnectionError as e:
        return show(user_ID)
    return responce


def lookup(users_ID):
    url = "https://api.twitter.com/1.1/users/lookup.json?"
    params = {
        "user_id": users_ID,
        "stringify_ids": "true"
        }
    oath, ID = create_oath_session("lookup")
    try:
        responce = oath.post(url, params = params)
        insert2database(ID, responce)
    except ConnectionError as e:
        return lookup(users_ID)
    return responce



def followers(userID):

    url = "https://api.twitter.com/1.1/followers/ids.json?"
    params = {
        "user_id": userID,
        "stringify_ids": "true"
        }
    oath, ID = create_oath_session("followers")
    try:
        responce = oath.get(url, params = params)
        #responce = oath.post(url, params = params)
        insert2database(ID, responce)
    except ConnectionError as e:
        return followers(userID)
    return responce


def friends(userID):
    url = "https://api.twitter.com/1.1/friends/ids.json?"
    params = {
        "user_id": userID,
        "stringify_ids": "true"
        }
    oath, ID = create_oath_session("friends")
    try:
        responce = oath.get(url, params = params)
        #responce = oath.post(url, params = params)
        insert2database(ID, responce)
    except ConnectionError as e:
        return friends(userID)
    return responce


def tweets(keyword, count):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": keyword,
        "lang": "ja",
        "result_type": "mixed",
        "count": count
        }
    oath, ID = create_oath_session("tweets")
    try:
        responce = oath.get(url, params = params)
        insert2database(ID, responce)
    except ConnectionError as e:
        return tweet(userID)
    return responce


def users(keyword, page, count):
    url = "https://api.twitter.com/1.1/users/search.json?"
    params = {
        "q": keyword,
        "page": page,
        "count": count
        }
    oath, ID = create_oath_session("users")
    try:
        responce = oath.get(url, params = params)
        insert2database(ID, responce)
    except ConnectionError as e:
        return tweet(userID)
    return responce


def insert2database(ID, responce):
    limit = responce.headers['x-rate-limit-remaining'] if 'x-rate-limit-remaining' in responce.headers else 0
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    Server_Mydatabase.update('api_limit', ((ID, str(limit), now, api)))


def limit_check(api_name):

    SQLs = Server_Mydatabase.select('select id, limited, last_use from api_limit where api_name = \'' + api_name + '\'')

    now = time.strftime('%Y-%m-%d %H:%M:%S')
    now_time = datetime.datetime(int(now[0:4]),int(now[5:7]),int(now[8:10]),int(now[11:13]),int(now[14:16]),int(now[17:19]))

    ID = ""

    for SQL in SQLs:
        limit = SQL[1]
        last_use = SQL[2]
        last_time = datetime.datetime(int(last_use[0:4]),int(last_use[5:7]),int(last_use[8:10]),int(last_use[11:13]),int(last_use[14:16]),int(last_use[17:19]))
        delta = now_time - last_time
        if int(limited) > 0 or delta.total_seconds() > 900:
            ID = SQL[0]
            break

    if ID = "":
        print("start sleep")
        sleep(900)
        ID = 1

    return ID


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
