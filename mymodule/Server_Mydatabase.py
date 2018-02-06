# coding: utf-8
from sshtunnel import SSHTunnelForwarder
import MySQLdb
import sys,os
import yaml

'''
# テーブルの作成
sql = 'create table test (id int, content varchar(32))'
c.execute(sql)
print('* testテーブルを作成\n')

# テーブル一覧の取得
sql = 'show tables'
c.execute(sql)
print('===== テーブル一覧 =====')
print(c.fetchone())

# レコードの削除
sql = 'delete from test where id=%s'
c.execute(sql, (2,))
print('\n* idが2のレコードを削除\n')

# レコードの取得
sql = 'select * from test'
c.execute(sql)
print('===== レコード =====')
for row in c.fetchall():
    print('Id:', row[0], 'Content:', row[1])
'''

def load_pass():
    f = open('../password/database.yml', 'r+')
    password = yaml.load(f)
    return password


def check(userID):

      password = load_pass()
      conn = MySQLdb.connect(user=password['database_user'],
          host=password['ip'],
          password=password['database_password'],
          db=password['dbname'])
      c = conn.cursor()
      sql = "SELECT state from checked_list where userID = " + userID
      c.execute(sql)
      result = c.fetchall()
      if len(result) == 0: return '***'
      return result[0][0]


def select(sql):

      password = load_pass()
      conn = MySQLdb.connect(user=password['database_user'],
          host=password['ip'],
          password=password['database_password'],
          db=password['dbname'])
      c = conn.cursor()
      c.execute(sql)
      result = c.fetchall()

      return result

def update(database, values):

      password = load_pass()
      conn = MySQLdb.connect(user=password['database_user'],
          host=password['ip'],
          password=password['database_password'],
          db=password['dbname'])
      c = conn.cursor()

      # レコードの更新

      if database == 'checked_list':
        c.execute('UPDATE checked_list SET state = \'' + values[0] +'\' WHERE userID= \'' + values[1] + '\'')
      elif database == 'api_limit':
        c.execute('UPDATE api_limit SET limited = \'' + str(values[1]) +'\', last_use = \'' + values[2] + '\' WHERE api_name = \'' + values[3] + '\' and id = \'' + str(values[0]) + '\'')
      # データベースへの変更を保存
      conn.commit()



def insert(database, values):

      password = load_pass()
      conn = MySQLdb.connect(user=password['database_user'],
          host=password['ip'],
          password=password['database_password'],
          db=password['dbname'])
      c = conn.cursor()

      # レコードの登録
      if database == "follow_graph": sql = 'INSERT ignore into follow_graph values (%s, %s)'
      elif database == 'checked_list': sql = 'INSERT ignore into checked_list values (%s, %s, %s, %s, %s)'
      elif database == 'query': sql = 'INSERT ignore into query values (%s, %s, %s, %s)'
      else: sql = 'INSERT ignore into result values (%s, %s, %s)'
      if isinstance(values,tuple): c.execute(sql, values)  # 1件のみ
      else: c.executemany(sql, values)    # 複数件
      print('\n* complete : insert\n')

      # データベースへの変更を保存
      conn.commit()

      c.close()
      conn.close()
