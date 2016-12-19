# coding=utf-8

import urllib2

f = urllib2.urlopen('http://httpbin.org/ip')
print f.read()

proxy_support = urllib2.ProxyHandler({"http" : "http://124.88.67.17:843"})
opener = urllib2.build_opener(proxy_support)

# install it
urllib2.install_opener(opener)

f = urllib2.urlopen('http://httpbin.org/ip')
print f.read()

