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
    sql_delete  = 'DELETE FROM session WHERE client_id = ?'
    sql_get     = 'SELECT * FROM session WHERE client_id = ?'

    def __init__(self):

        self.new  = False
        self.conn = None
        self.path = os.path.join(os.getcwd()+self.config('sessionpath'))
        self.db   = self.config('dbname')

        """ Create db if file doesn't exist """
        if not os.path.exists(self.path+self.db):
            with self.dbconn() as conn:
                conn.execute(self.sql_create_tbl)
                self.new = True

    def config(self,option):
        """ Reads config file """
        config = ConfigParser()
        config.read('Align/config.ini')
        return config.get('apiConfig',option)

    def dbconn(self):
        """ Database connection """
        if not self.conn:
            self.conn = sqlite3.Connection(self.path+self.db)
        return self.conn

    def dbclose(self):
        """ Close database connection """
        self.conn.close()

    def get(self,client_id):
        """ Get session data """
        conn = self.dbconn().cursor()
        conn.execute(self.sql_get,(client_id,))
        return conn.fetchone()

    def create(self,data):  
        """ Create session data """      
        with self.dbconn() as conn:
            conn.execute(self.sql_delete,(self.config('clientid'),))
            conn.execute(self.sql_create,(data['access_token'], self.config('clientid'), data['expires']))
            self.conn.commit()

    def convertTimestamp(self,timestamp):
        """ Convert timestamp to Y-m-d H:i:s date format """
        value = datetime.fromtimestamp(timestamp)
        return value.strftime('%Y-%m-%d %H:%M:%S')

    #check if token is expired
    def isTokenExpired(self,timestamp):
        """ Check if access token is expired (expiry date is in timestamp format)"""
        expiry  = datetime.fromtimestamp( int(timestamp) )
        now     = datetime.fromtimestamp( int(time.time()) )

        return expiry < now
