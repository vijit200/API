import pymongo
class mongo():
    def __init__(self,link,database,table):
        self.link = link
        self.database = database
        self.table = table

    def mong_con(self):
        try:

            self.my_db = pymongo.MongoClient('{}'.format(self.link),tls = True,tlsAllowInvalidCertificates= True)
            self.db = self.my_db['{}'.format(self.database)]
            self.col1 = self.db['{}'.format(self.table)]
            self.l = []
            for i in self.col1.find():
                self.l.append(i)
            return self.l
        except Exception as e:
            return e