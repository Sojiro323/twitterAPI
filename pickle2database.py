from mymodule import MytwitterAPI
from mymodule import Mypickle
from mymodule import Mydatabase

path = "./pickle/"
load_files = Mypickle.load(path, ['friends_dic','followers_dic'])
friends_dic = load_files[0]
followers_dic = load_files[1]

print(len(friends_dic),len(followers_dic))

values = []
for user,friends in friends_dic.items():
    for friend in friends:
        values.append((user,friend))


for user,followers in followers_dic.items():
    for follower in followers:
        values.append((follower,user))

print(len(values))
Mydatabase.insert("follow_graph", values)
