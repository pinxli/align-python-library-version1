import pycurl, urllib, sys, json, cStringIO
from urllib import urlencode
from ConfigParser import ConfigParser

class Curl ():

	def __init__(self):
		self.headers = []
		self.options = []
		self.request = ''

		self.url 				= self.config('apiurl')
		self.authBasicUsername  = self.config('username')
		self.authBasicPassword  = self.config('password')

	def get(self, url, data=None):
		return self.curlrequest('get', self.url+url+'?'+urlencode(data), data)

	def post(self, url, data=None):
		return self.curlrequest('post', self.url+url, data)

	def put(self, url, data=None):
		return self.curlrequest('put', self.url+url, data)

	def curlrequest(self, method,url,data=None):
		response = cStringIO.StringIO()

		self.request = pycurl.Curl()
		self.httpLogin()
		self.setRequestMethod(method,data)
		self.setRequestOptions(url)
		self.request.setopt(self.request.WRITEFUNCTION, response.write)
		self.request.perform()
		self.request.close()
		return response.getvalue()

	def setRequestMethod(self,method,data=None):
		method = method.upper()

		if (method == 'GET'):
			self.request.setopt(pycurl.HTTPGET, True)
		elif (method == 'POST'):
			# data = urlencode(data)
			data = json.dumps(data)

			self.request.setopt(pycurl.CUSTOMREQUEST, method)
			self.request.setopt(pycurl.POST, True)
			self.request.setopt(pycurl.POSTREDIR,3)
			self.request.setopt(pycurl.POSTFIELDS, data)
			self.request.setopt(pycurl.HTTPHEADER, [
				'Accept: application/json',
				'Content-Type: application/json; charset=utf-8',
				'Connection: Keep-Alive'])

		elif (method == 'PUT'):
			# data = urlencode(data)
			data = json.dumps(data)
			self.request.setopt(pycurl.CUSTOMREQUEST, method)
			self.request.setopt(pycurl.POST, True)
			self.request.setopt(pycurl.POSTFIELDS, data)
			self.request.setopt(pycurl.HTTPHEADER, [
				'Accept: application/json',
				'Content-Type: application/json; charset=utf-8',
				'Connection: Keep-Alive'])
		elif (method == 'DELETE'):
			self.request.setopt(pycurl.CUSTOMREQUEST, method)

	def setRequestOptions(self,url):
		self.request.setopt(pycurl.URL, url)
		self.request.setopt(pycurl.FOLLOWLOCATION, True)
		
	def httpLogin(self):
		self.request.setopt(pycurl.VERBOSE, 0)
		self.request.setopt(pycurl.USERPWD, self.authBasicUsername + ':' + self.authBasicPassword)

	def config(self,option):
		config = ConfigParser()
		config.read('Align/config.ini')
		return config.get('apiConfig',option)



