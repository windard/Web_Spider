# coding=utf-8

import urllib
import urllib2

f = urllib2.urlopen('ftp://admin:password@127.0.0.1/test.txt')

print f.read()

urllib.urlretrieve('ftp://admin:password@127.0.0.1/test.txt', 'test.txt')

print "Download successful ~"