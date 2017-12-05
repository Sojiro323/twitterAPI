# coding: utf-8

import MySQLdb
import sys,os

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

DBNAME = 'twitterDB'


def check(userID):

    conn = MySQLdb.connect(user="root",host="localhost",password="23622059",db=DBNAME) 
    c = conn.cursor()
    sql = "select state from checked_list where userID = " + userID
    c.execute(sql)
    result = c.fetchall()
    if len(result) == 0: result = '***'
    return result


def select(sql):
    
    conn = MySQLdb.connect(user="root",host="localhost",password="23622059",db=DBNAME) 
    c = conn.cursor()
    c.execute(sql)
    result = c.fetchall()
    
    return result




def insert(database, values):
    conn = MySQLdb.connect(user="root",host="localhost",password="23622059",db=DBNAME)
    c = conn.cursor()

    # レコードの登録
    if database == "follow_graph": sql = 'insert ignore into follow_graph values (%s, %s)'
    elif database == 'checked_list': sql = 'insert ignore into checked_list values (%s, %s, %s, %s, %s)'
    else: sql = 'insert ignore into result values (%s, %s, %s)'
    if isinstance(values,tuple): c.execute(sql, values)  # 1件のみ
    else: c.executemany(sql, values)    # 複数件
    print('\n* complete : insert\n')

    # データベースへの変更を保存
    conn.commit()

    c.close()
    conn.close()
