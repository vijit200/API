import mysql.connector as conn
class my_con():
    def __init__(self,host,user,passwd,database,table):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.table = table

    def connection(self):
        try:
            self.my_db = conn.connect(host = self.host,user = self.user,passwd = self.passwd,use_pure=True)
            self.cur = self.my_db.cursor()
            self.cur.execute('USE {}'.format(self.database))
            self.cur.execute('SELECT * FROM {}'.format(self.table))
            self.l = []
            for i in self.cur.fetchall():
                self.l.append(i)
            return self.l
        except Exception as e:
            return e
