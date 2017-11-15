# coding: utf-8

import MySQLdb
import sys,os

DBNAME = 'twitter'


def main():
    conn = MySQLdb.connect(user="root",host="localhost",password="23622059",db=DBNAME)
    c = conn.cursor()

    # テーブルの作成
    sql = 'create table test (id int, content varchar(32))'
    c.execute(sql)
    print('* testテーブルを作成\n')

    # テーブル一覧の取得
    sql = 'show tables'
    c.execute(sql)
    print('===== テーブル一覧 =====')
    print(c.fetchone())

    # レコードの登録
    sql = 'insert into test values (%s, %s)'
    c.execute(sql, (1, 'hoge'))  # 1件のみ
    datas = [
        (2, 'foo'),
        (3, 'bar')
    ]
    c.executemany(sql, datas)    # 複数件
    print('\n* レコードを3件登録\n')

    # レコードの取得
    sql = 'select * from test'
    c.execute(sql)
    print('===== レコード =====')
    for row in c.fetchall():
        print('Id:', row[0], 'Content:', row[1])

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

    # データベースへの変更を保存
    conn.commit()

    c.close()
    conn.close()


if __name__ == '__main__':
    main()
