#coding=utf-8
import urllib2
url = 'http://www.baidu.com'
#加入http请求的请求者地址，此处是本人的chrome 45.0.2454.12
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.12 Safari/537.36'
#封装成http请求头
headers = {'User-Agent':user_agent}
#将http请求头加入到Request中，组装成一个完整的请求
req = urllib2.Request(url=url,headers=headers)
#此时urlopen就不再是直接请求URL了，而是请求已经封装好了的Req对象
page = urllib2.urlopen(req)
html = page.read()
print html