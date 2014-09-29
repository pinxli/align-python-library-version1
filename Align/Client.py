from Curl import Curl
from SqliteSession import SqliteSession
import json, sys, inspect
from urllib import urlencode

class Client():

	def __init__(self, client_id, secret_key):

		""" Check session """
		self.session = SqliteSession()
		client_id 	 = self.session.config('clientid')

		if( self.session.get(client_id) ):
			""" Get access token from sqlite session """
			res = self.session.get(client_id)
		else:
			""" Request new access token and store it to sqlite session """
			self.getAccessToken(client_id, secret_key)
			res = self.session.get(client_id)

		self.access_token = res[0]
		self.expiry 	  = res[2]

		is_expired = self.session.isTokenExpired(self.expiry)

		""" Request new access token and store it to sqlite session """
		if ( is_expired ):
			self.getAccessToken(client_id, secret_key)

	def request(self, method, url, data=None):
		"""
		Generic request
		@parameter method: get, put, post
		@parameter url: api url'
		@parameter data: data for post and put method
		"""
		curl = Curl()

		if data is not None:
			data['access_token'] = self.access_token
		else:
			data = { 'access_token' : self.access_token }

		if( method == 'post' ):
			res = curl.post(url,data)

		elif( method == 'put' ):
			res = curl.put(url,data)

		else:
			res = curl.get(url,data)

		return res

	def buyer(self,method,data=None,param=None):
		"""
		Buyer method
		@parameter method: list, info, create
		@parameter data: accepts str or dict
		@parameter param: accepts dict
		"""
		res = None

		if( method == 'list' ):
			res = self.request('get','buyer/')

		elif( method == 'info' ):
			if ( type(data).__name__ == 'str' ):
				res = self.request('get','buyer/'+data)

		elif( method == 'create' ):
			if ( type(data).__name__ == 'dict' ):
				res = self.request('post','buyer/',data)

		return res

	def invoice(self,method,data=None,param=None):
		"""
		Invoice method
		@parameter method: list, info, create
		@parameter data: it accepts str or dict
		@parameter param: accepts dict
		"""
		res = None

		if( method == 'list' ):
			res = self.request('get','invoice/')

		elif( method == 'info' ):
			if ( type(data).__name__ == 'str' ):
				res = self.request('get','invoice/'+data)

		elif( method == 'create' ):
			if ( type(data).__name__ == 'dict' ):
				res = self.request('post','invoice/',data)

		return res

	def product(self,method,data=None,param=None):
		"""
		Product method
		@parameter method: list, info, create
		@parameter data: it accepts str or dict
		@parameter param: accepts dict
		"""
		res = None

		if( method == 'list' ):
			res = self.request('get','products/')

		elif( method == 'info' ):
			if ( type(data).__name__ == 'str' ):
				res = self.request('get','products/'+data)

		elif( method == 'update' ):
			if ( type(data).__name__ == 'str' and type(param).__name__ == 'dict' ):
				res = self.request('put','products/'+data,param)

		elif( method == 'create' ):
			if ( type(data).__name__ == 'dict' ):
				res = self.request('post','products/',data)

		return res

	def getAccessToken(self, client_id, secret_key):
		"""
		Request access token and saves it in sqlite session
		"""
		c = Curl()
		param = {
			'grant_type'    : self.session.config('granttype'),
			'client_id'     : client_id,
			'client_secret' : secret_key,
			'scope'         : self.session.config('scope')
		}

		res = json.loads(c.post('oauth/access_token',param))

		return self.session.create(res)

