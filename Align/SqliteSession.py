import sha, shelve, time, Cookie, os, sqlite3
from uuid import uuid4
from Curl import Curl
from ConfigParser import ConfigParser

class SqliteSession():

    sql_create = (
        """
        CREATE TABLE IF NOT EXISTS session
        (
            access_token TEXT PRIMARY KEY,
            expiry BIGINT
        )
        """
    )
    sql_create  = 'INSERT INTO session VALUES (?,?,?)'
    sql_get     = 'SELECT * FROM session WHERE key = ?'

    def __init__(self):
        self.conn = None
        self.path = os.path.join(os.getcwd()+self.config('sessionpath'))

        if not os.path.exists(self.path):
            with self.dbconn() as conn:
                conn.execute(self.sql_create)

    def config(self,option):
        config = ConfigParser()
        config.read('Align/config.ini')
        return config.get('apiConfig',option)

    def dbconn(self):
        if not self.conn:
            self.conn = sqlite3.Connection(self.path)
        return self.conn

    def get(self,data):
        with self.dbconn as conn:
            res = conn.execute(self.sql_get,(data['access_token']))
        return res

    def create(self,data):
        with self.dbconn as conn:
            conn.execute(self.sql_create,(data['access_token'],data['expiry']))

    def getAccessToken(self):
        c = Curl()
        param = {
            'grant_type'    : self.config('granttype'),
            'client_id'     : self.config('clientid'),
            'client_secret' : self.config('secretkey'),
            'scope'         : self.config('scope')
        }

        res = c.post('oauth/access_token',param)
        # print(res)