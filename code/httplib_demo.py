#coding=utf-8

import httplib

#建立一个HTTPConnection对象
conn1 = httplib.HTTPConnection('192.168.137.1')
#发送GET请求
conn1.request('GET','/test.php')
#得到一个HTTPResponse对象
res1 = conn1.getresponse()

#打印页面内容
print res1.read()

#得到返回响应头
head = res1.getheaders()

#打印返回响应头
for i,j in head:
	print i+"  :  "+j

#打印返回对象的msg属性
print res1.msg

#打印返回对象的状态码
print res1.status

#打印返回对象的version
print res1.version

#打印返回对象的reason
print res1.reason

conn1.close()

