import pycurl
import urllib
from Config.Apiconfig import Apiconfig

class Curl (Apiconfig):

	def __init__(self):
		self.headers = []
		self.options = []
		self.request = ''
		self.authBasicUsername  = Apiconfig.authBasicUsername
		self.authBasicPassword  = Apiconfig.authBasicPassword

	def get(self,url,vars=None):
		self.curlrequest('get', url, vars)

	def post(self, url , vars=None):
		self.curlrequest('post', url, vars)

	def put(self,url,vars=None):
		self.curlrequest('put', url, vars)

	def delete(self,url,vars=None):
		self.curlrequest('delete', url, vars)

	def curlrequest(self, method,url,vars=None):
		self.request = pycurl.Curl()
		self.httpLogin()
		self.setRequestMethod(method)
		self.setRequestOptions(url,vars)
		self.request.perform()

	def setRequestMethod(self,method):
		if (method.lower() == 'get'):
			self.request.setopt(pycurl.HTTPGET, True)
		elif (method.lower() == 'post'):
			self.request.setopt(pycurl.CUSTOMREQUEST, method.upper())
			self.request.setopt(pycurl.POST, True)
			self.request.setopt(pycurl.POSTREDIR,3)
		elif (method.lower() == 'put'):
			self.request.setopt(pycurl.CUSTOMREQUEST, method.upper());
		elif (method.lower() == 'delete'):
			self.request.setopt(pycurl.CUSTOMREQUEST, method.upper());

	def setRequestOptions(self,url,vars):
		self.request.setopt(pycurl.URL, url)
		self.request.setopt(pycurl.FOLLOWLOCATION, True)
		
	def httpLogin(self):
		self.request.setopt(pycurl.VERBOSE, 0)
		self.request.setopt(pycurl.USERPWD, self.authBasicUsername + ':' + self.authBasicPassword)



