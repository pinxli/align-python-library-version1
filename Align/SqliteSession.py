import sha, shelve, time, Cookie, os, sqlite3, json, sys
from uuid import uuid4
from Curl import Curl
from ConfigParser import ConfigParser
from datetime import datetime, date

class SqliteSession():

    sql_create_tbl = (
        """
        CREATE TABLE IF NOT EXISTS session
        (
            access_token TEXT,
            client_id TEXT,
            expiry BIGINT
        )
        """
    )
    sql_create  = 'INSERT INTO session VALUES (?,?,?)'
    sql_get     = 'SELECT expiry FROM session WHERE client_id = ?'

    def __init__(self):

        self.new  = False
        self.conn = None
        self.path = os.path.join(os.getcwd()+self.config('sessionpath'))
        self.db   = self.config('dbname')

        #create db if file doesn't exist
        if not os.path.exists(self.path+self.db):
            with self.dbconn() as conn:
                conn.execute(self.sql_create_tbl)
                self.new = True

    def config(self,option):
        config = ConfigParser()
        config.read('Align/config.ini')
        return config.get('apiConfig',option)

    #db connection
    def dbconn(self):
        if not self.conn:
            self.conn = sqlite3.Connection(self.path+self.db)
        return self.conn

    #db close
    def dbclose(self):
        self.conn.close()

    #get session data
    def get(self,client_id):
        conn = self.dbconn().cursor()
        conn.execute(self.sql_get,(client_id,))
        return conn.fetchone()

    #create session data
    def create(self,data):        
        with self.dbconn() as conn:
            conn.execute(self.sql_create,(data['access_token'], self.config('clientid'), data['expires']))
            self.conn.commit()

    #convert timestamp to Y-m-d H:i:s date format
    def convertTimestamp(self,timestamp):
        value = datetime.fromtimestamp(timestamp)
        return value.strftime('%Y-%m-%d %H:%M:%S')

    #check if token is expired
    def isTokenExpired(self,timestamp):
        #timestamp
        expiry  = datetime.fromtimestamp( int(timestamp) )
        now     = datetime.fromtimestamp( int(time.time()) )

        return expiry < now

    #request new access token
    def getAccessToken(self):
        c = Curl()
        param = {
            'grant_type'    : self.config('granttype'),
            'client_id'     : self.config('clientid'),
            'client_secret' : self.config('secretkey'),
            'scope'         : self.config('scope')
        }

        res = json.loads(c.post('oauth/access_token',param))
        
        return self.create(res)
        # if self.new:
        #     return self.create(res)
        # else:
        #     return self.new
