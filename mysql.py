# -*-coding:utf-8-*-
import json
from os.path import abspath, dirname, join
import MySQLdb


class MysqlHandler(object):
    def __init__(self, host, port, user, passwd, db):
        self.conn = None
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db

    def login(self):
        try:
            self.conn = MySQLdb.connect(
                user=self.user, passwd=self.passwd, host=self.host,
                port=self.port, db=self.db, charset="utf8")
            return True
        except Exception:
            return False

    def logout(self):
        try:
            self.conn.close()
            return True
        except Exception:
            return False

    def query(self, sql):
        raws = tuple()
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            raws = cur.fetchall()
            cur.close()
        except Exception:
            pass
        finally:
            return raws

    def update(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return True
        except Exception:
            return False

    def insert(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return True
        except Exception:
            return False

    def delete(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            return True
        except Exception:
            return False


def set_db_conf(db_conf):
    with open(db_conf, 'r') as f:
        return json.load(f)


BASE_DIR = dirname(abspath(__file__))

db_conf = join(BASE_DIR, 'db.conf')
db = set_db_conf(db_conf)
db_host = db.get('host', None)
db_port = db.get('port', None)
db_user = db.get('user', None)
db_password = db.get('password', None)
db_name = db.get('database', None)

mysql = MysqlHandler(db_host, db_port, db_user, db_password, db_name)

print mysql.login()
sql = ""
print mysql.query(sql)
# print mysql.update(sql)
# print mysql.insert(sql)
# print mysql.delete(sql)
print mysql.logout()
