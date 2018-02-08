# -- coding: utf-8 --
def load_pass():
    import yaml
    f = open('../password/database.yml', 'r+')
    password = yaml.load(f)
    return password

def init():
    import MySQLdb
    password = load_pass()
    conn = MySQLdb.connect(user=password['database_user'],
        host=password['ip'],
        password=password['database_password'],
        db=password['dbname'])

    return conn
