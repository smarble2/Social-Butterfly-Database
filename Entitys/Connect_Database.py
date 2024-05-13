#coonect to mySQL

import mysql.connector

class Connect_Database:
    # make connection
    def __init__(self):
        self.conn = mysql.connector.connect(user='TTSUser',password='osboxes.org',host='127.0.0.1', database='SBA')

    def getConnection(self):
        return self.conn

    def close(self):
        self.conn.close()