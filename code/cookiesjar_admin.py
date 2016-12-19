# coding=utf-8

import urllib2
import cookielib

cookie = cookielib.CookieJar()
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)

result = opener.open("http://127.0.0.1/cookies.php")

print result.read()

for item in cookie:
	print item.name, ":", item.value

# 清除之前的 cookies
cookie.clear()

# 新建一个新的我们的 cookies
c = cookielib.Cookie(version=0, name='user', value='admin', port=None, port_specified=False, domain='127.0.0.1', domain_specified=False, domain_initial_dot=False, path='/', path_specified=False, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)

# 将新的 cookies 添加到 CookieJar 中
cookie.set_cookie(c)

result = opener.open("http://127.0.0.1/cookies.php")

print result.read()