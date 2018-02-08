# coding: utf-8
#import pymysql
#pymysql.install_as_MySQLdb()
import MySQLdb
from . import prepare



def check(userID):

    conn = prepare.init()
    
    c = conn.cursor()
    sql = "SELECT state from checked_list where userID = " + userID
    c.execute(sql)
    
    result = c.fetchall()
    c.close()

    if len(result) == 0: return '***'
    return result[0][0]


def select(sql):

    conn = prepare.init()
    c = conn.cursor()
    c.execute(sql)
    result = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    return result

def update(database, values):

    conn = prepare.init()
    c = conn.cursor()

    if database == 'checked_list':
        c.execute('UPDATE checked_list SET state = \'' + values[0] +'\' WHERE userID= \'' + values[1] + '\'')
    elif database == 'api_limit':
        c.execute('UPDATE api_limit SET limited = \'' + str(values[1]) +'\', last_use = \'' + values[2] + '\' WHERE api_name = \'' + values[3] + '\' and id = \'' + str(values[0]) + '\'')
    else:
        print("database is failed")
    # データベースへの変更を保存
    conn.commit()
    c.close()
    conn.close()


def insert(database, values):

    conn = prepare.init()
    c = conn.cursor()

    # レコードの登録
    if database == "follow_graph": sql = 'INSERT ignore into follow_graph values (%s, %s)'
    elif database == 'checked_list': sql = 'INSERT ignore into checked_list values (%s, %s, %s, %s, %s)'
    elif database == 'query': sql = 'INSERT ignore into query values (%s, %s, %s, %s)'
    elif database == 'api_limit': sql = 'INSERT into api_limit values (%s, %s, %s, %s)'
    else: sql = 'INSERT ignore into result values (%s, %s, %s)'
    if isinstance(values,tuple): c.execute(sql, values)  # 1件のみ
    else: c.executemany(sql, values)    # 複数件

    # データベースへの変更を保存
    conn.commit()

    c.close()
    conn.close()

def register_api():
    import os
    MAX = select("select MAX(id) from api_limit")[0][0]
    keys = os.listdir('../password/twitterAPI/')

    f = open('../password/API_database.yml', 'r+')
    api_names = yaml.load(f)['api_name']

    for key in keys:
      if 'yml' not in key: continue
      ID = key.split(".")[0]
      if int(ID) > MAX:
        for api_name in api_names:
          insert("api_limit", (ID,api_name,0,'2018-01-01 00:00:00'))
