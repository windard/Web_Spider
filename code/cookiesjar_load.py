# coding=utf-8

import urllib
import urllib2
import cookielib

# 使用刚才已保存的 cookies.txt
cookie = cookielib.MozillaCookieJar()

cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)

handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)

# 打印 cookies

for item in cookie:
	print item.name, ":", item.value

result = opener.open("http://127.0.0.1/login.php")

print result.read()

# 再次登录

data={
    "username":"windard",
    "password":"password",
    "submit":"submit"
}

postdata = urllib.urlencode(data)

headers ={
    "Host":"127.0.0.1", 
    "Referer":"http://127.0.0.1/login.php",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}

req = urllib2.Request("http://127.0.0.1/login.php", postdata, headers)

cookie.clear()

result = opener.open(req)

# 再次打印结果
result = opener.open("http://127.0.0.1/login.php")
print result.read()
