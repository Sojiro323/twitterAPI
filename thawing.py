# coding: utf-8
from sshtunnel import SSHTunnelForwarder
import MySQLdb
import sys,os
import yaml
import gzip
import os

f = open('../password/database.yml', 'r+')
password = yaml.load(f)

def insert(values):
  

  conn = MySQLdb.connect(user=password['database_user'],
    host=password['ip'],
    password=password['database_password'],
    db=password['dbname'])
  c = conn.cursor()

  # レコードの登録
  sql = 'INSERT ignore into old_follow_graph values' + values
  c.execute(sql)
  conn.commit()

  c.close()
  conn.close()



values = ''
count = 0
followers_path = "../order_follower_ja_inter_zip/"
friends_path = "../order_friend_ja_inter_zip/"

while(1):
  print("input friend or follower")
    
  d = input('>>> ')

  if d == "friend" or d == "follower": break
  else: "\ninput again!!\n\n"

if d == 'friend':
  files = os.listdir(followers_path)

  for f in files:
    with gzip.open(followers_path + f, "rb") as ff:
      for line in ff:
        line = line.decode('utf-8').split('\t')
        user = line[0]
        follower = line[1].replace('\n','')
        values += '(\'' + user + '\',\'' + follower + '\'),'
        count += 1
        if count == 1000:
          insert(values[:-1])
          values = ""
          count = 0
  j = open('follower.txt' , 'a')
  j.write(f + '\n')
  j.close()


else:

  files = os.listdir(friends_path)
  for f in files:
    with gzip.open(friends_path + f, "rb") as ff:
      for line in ff:
        line = line.decode('utf-8').split('\t')
        follower = line[1].replace('\n','')
        user = line[0]
        values += '(\'' + user + '\',\'' + follower + '\'),'
        count += 1
        if count == 1000:
          insert(values[:-1])
          values = ""
          count = 0
  j = open('friend.txt' , 'a')
  j.write(f + '\n')
  j.close()
