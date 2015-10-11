# coding=utf8
#导入urllib库
import urllib
#设定将要请求的URL地址
url = 'http://www.baidu.com'
#其实重点就这一句
page = urllib.urlopen(url)
#读取接收到的返回信息
info = page.info()
#打印出来
print "Info:"
print info
#读取接收到的返回状态码
code = page.getcode()
#打印出来
print "Code:"
print code
