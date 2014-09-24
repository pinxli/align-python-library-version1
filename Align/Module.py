from Curl import Curl
from SqliteSession import SqliteSession
import json, sys, inspect

class Module():

	def __init__(self):

		#check session
		session = SqliteSession()
		
		client_id = session.config('clientid')

		#check if clientid in session exists
		if( session.get(client_id) ):
			res = session.get(client_id)
		else:
			session.getAccessToken()
			res = session.get(client_id)

		is_expired = session.isTokenExpired(res[0])

		if ( is_expired):
			session.getAccessToken()

	def request(self,module,method,data=None):
		curl = Curl()

		if( method == 'post' ):
			res = curl.post(module,data)
		elif( method == 'put' ):
			res = curl.get(module,data)
		else:
			res = curl.get(module,data)

		return res

	def invoice(self,method,data=None):
		res = None

		if( method == 'info' ):
			if ( type(data).__name__ == 'str' ):
				res = self.request('invoice','get',data)
		elif( method == 'create' ):
			if ( type(data).__name__ == 'dict' ):
				res = self.request('invoice','post',data)
		else:
			res = self.request('invoice','get')

		return res

	def product(self,method,data=None):
		res = None

		if( method == 'info' ):
			if ( type(data).__name__ == 'str' ):
				res = self.request('products','get',data)
		elif( method == 'create' ):
			if ( type(data).__name__ == 'dict' ):
				res = self.request('products','post',data)
		else:
			res = self.request('products','get')

		return res

