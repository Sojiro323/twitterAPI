import gzip
import os


def insert(values):
  
  password = load_pass()

  conn = MySQLdb.connect(user=password['database_user'],
    host=password['ip'],
    password=password['database_password'],
    port=ssh.local_bind_port,
    db=password['dbname'])
  c = conn.cursor()

  # レコードの登録
  sql = 'INSERT ignore into follow_graph_old values (%s, %s)'
  if isinstance(values,tuple): c.execute(sql, values)  # 1件のみ
  else: c.executemany(sql, values)    # 複数件
  print('\n* complete : insert\n')

  conn.commit()

  c.close()
  conn.close()




values = []
followers_path = "../order_follower_ja_inter_zip/"
friends_path = "../order_friend_ja_inter_zip/"

files = os.listdir(followers_path)

for f in files:
  with gzip.open(followers_path + f, "rb") as ff:
    for line in ff:
      line = line.decode('utf-8').split('\t')
      user = line[0]
      follower = line[1].replace('\n','')
      values.append([user, follower])
      break
  break

#insert(values)

values = []

files = os.listdir(friends_path)


for f in files:
  with gzip.open(friends_path + f, "rb") as ff:
    for line in ff:
      line = line.decode('utf-8').split('\t')
      follower = line[1].replace('\n','')
      user = line[0]
      print(user, follower)
      values.append([user, follower])
      break
    break

#insert(values)
