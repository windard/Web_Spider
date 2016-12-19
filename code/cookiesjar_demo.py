# coding=utf-8

import urllib2
import cookielib

cookie = cookielib.CookieJar()
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)

opener.open("https://www.baidu.com")

# print cookie

for item in cookie:
	print item.name, ":", item.value