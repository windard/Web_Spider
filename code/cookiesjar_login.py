# coding=utf-8

import urllib
import urllib2
import cookielib

# 使用 MozillaCookieJar 来保存 cookies
cookie = cookielib.MozillaCookieJar("cookies.txt")

handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)

result = opener.open("http://127.0.0.1/login.php")

print result.read()

postdata = urllib.urlencode({
	'username':'中国人',
	'password':'password',
	'submit':'submit'
	})

print postdata

result = opener.open("http://127.0.0.1/login.php", postdata)

print result.read()

# 保存 cookies
cookie.save(ignore_discard=True, ignore_expires=True)

# 再次访问

result = opener.open("http://127.0.0.1/login.php")

print result.read()

# 打印 cookies

for item in cookie:
	print item.name, ":", item.value