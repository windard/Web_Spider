# coding=utf-8

import urllib2

try:
	f = urllib2.urlopen('http://127.0.0.1:5000/secret-page')
except Exception,e:
	print e

# set up authentication info
authinfo = urllib2.HTTPBasicAuthHandler()
authinfo.add_password(realm="Login Required", uri="http://127.0.0.1:5000/secret-page", user='admin', passwd='secret')

# build a new opener that adds authentication and caching FTP handlers
opener = urllib2.build_opener(authinfo)

# install it
urllib2.install_opener(opener)

f = urllib2.urlopen('http://127.0.0.1:5000/secret-page')

print f.read()
