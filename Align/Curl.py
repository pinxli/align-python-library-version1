import pycurl, urllib, sys, json
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

	def get(self, module=None, data=None):
		url = self.cleanUrl(module,data)
		return self.curlrequest('get', url, data)

	def post(self, module=None, data=None):
		url = self.cleanUrl(module)
		return self.curlrequest('post', url, data)

	def put(self,module=None,data=None):
		id 	 = data['id']
		data = data['data']
		url  = self.cleanUrl(module,id)
		return self.curlrequest('put', url, data)

	def delete(self,module=None,data=None):
		url = self.cleanUrl(module)
		return self.curlrequest('delete', url, data)

	def curlrequest(self, method,url,data=None):
		self.request = pycurl.Curl()
		self.httpLogin()
		self.setRequestMethod(method,data)
		self.setRequestOptions(url)
		return self.request.perform()
		# self.curl_storage.append(curl)

	def setRequestMethod(self,method,data=None):
		method = method.upper()

		if (method == 'GET'):
			self.request.setopt(pycurl.HTTPGET, True)
		elif (method == 'POST'):
			data = urlencode(data)
			self.request.setopt(pycurl.CUSTOMREQUEST, method)
			self.request.setopt(pycurl.POST, True)
			self.request.setopt(pycurl.POSTREDIR,3)
			self.request.setopt(pycurl.POSTFIELDS, data)
		elif (method == 'PUT'):
			data = urlencode(data)
			self.request.setopt(pycurl.CUSTOMREQUEST, method)
			self.request.setopt(pycurl.POST, True)
			self.request.setopt(pycurl.POSTFIELDS, data)
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

	def cleanUrl(self,module,data=None):
		url = self.url + module if module != None else self.url
		url = url + '/' + data if data != None else url
		return url



