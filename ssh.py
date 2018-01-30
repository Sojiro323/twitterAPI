# -*- coding: utf-8 -*-
from sshtunnel import SSHTunnelForwarder
# モジュール読み込み
import MySQLdb
import sys,os
import yaml

f = open('./password/database.yml', 'r+')
password = yaml.load(f)
print(password)

# SSH関連の設定
with SSHTunnelForwarder(
    (password['host'], password['local_port']),
    ssh_host_key= None,
    ssh_pkey=None,
    ssh_username=password['ssh_username'],
    ssh_password=password['ssh_password'],
    remote_bind_address=(password['ip'], password['database_port'])
    ) as ssh:

    print(ssh.local_bind_port)

    conn = MySQLdb.connect(
        user=password['database_user'],
        host=password['ip'],
        password=password['database_password'],
        port=ssh.local_bind_port,
        db=password['dbname']
        )

    c = conn.cursor()
    c.execute("select * from query")
    print(c.fetchall())
