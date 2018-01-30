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

open f = ('../../password/database.yml', 'r+'):
password = yaml.load(f)


def check(userID):

    with SSHTunnelForwarder(
      (password[host], password[local_port]),
      ssh_host_key= None,
      ssh_pkey=None,
      ssh_username=password[ssh_username],
      ssh_password=password[ssh_password],
      remote_bind_address=(password[ip], password[database_port])
      ) as ssh:

      conn = MySQLdb.connect(user=password[database_user],
          host=password[database_host],
          password=password[database_password],
          port=ssh.local_bind_port,
          db=password[dbname])
      c = conn.cursor()
      sql = "select state from checked_list where userID = " + userID
      c.execute(sql)
      result = c.fetchall()
      if len(result) == 0: return '***'
      return result[0][0]


def select(sql):

    with SSHTunnelForwarder(
      (password[host], password[local_port]),
      ssh_host_key= None,
      ssh_pkey=None,
      ssh_username=password[ssh_username],
      ssh_password=password[ssh_password],
      remote_bind_address=(password[ip], password[database_port])
      ) as ssh:

      conn = MySQLdb.connect(user=password[database_user],
          host=password[database_host],
          password=password[database_password],
          port=ssh.local_bind_port,
          db=password[dbname])
      c = conn.cursor()
      c.execute(sql)
      result = c.fetchall()

      return result

def update(database, values):

    with SSHTunnelForwarder(
      (password[host], password[local_port]),
      ssh_host_key= None,
      ssh_pkey=None,
      ssh_username=password[ssh_username],
      ssh_password=password[ssh_password],
      remote_bind_address=(password[ip], password[database_port])
      ) as ssh:

      conn = MySQLdb.connect(user=password[database_user],
          host=password[database_host],
          password=password[database_password],
          port=ssh.local_bind_port,
          db=password[dbname])
      c = conn.cursor()

      # レコードの更新

      if database == 'checked_list':
        c.execute('INSERT INTO checked_list (userID, state) VALUES (%s,%s) ON DUPLICATE KEY UPDATE userID=%s',values)
      elif database == 'api_limit':
        c.execute('INSERT INTO api_limit (api_name, limited, last_use) VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE api_name=%s',values)
      # データベースへの変更を保存
      conn.commit()



def insert(database, values):

    with SSHTunnelForwarder(
      (password[host], password[local_port]),
      ssh_host_key= None,
      ssh_pkey=None,
      ssh_username=password[ssh_username],
      ssh_password=password[ssh_password],
      remote_bind_address=(password[ip], password[database_port])
      ) as ssh:

      conn = MySQLdb.connect(user=password[database_user],
          host=password[database_host],
          password=password[database_password],
          port=ssh.local_bind_port,
          db=password[dbname])
      c = conn.cursor()

      # レコードの登録
      if database == "follow_graph": sql = 'insert ignore into follow_graph values (%s, %s)'
      elif database == 'checked_list': sql = 'insert ignore into checked_list values (%s, %s, %s, %s, %s)'
      elif database == 'query': sql = 'insert ignore into query values (%s, %s, %s, %s)'
      else: sql = 'insert ignore into result values (%s, %s, %s)'
      if isinstance(values,tuple): c.execute(sql, values)  # 1件のみ
      else: c.executemany(sql, values)    # 複数件
      print('\n* complete : insert\n')

      # データベースへの変更を保存
      conn.commit()

      c.close()
      conn.close()
