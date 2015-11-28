#coding=utf-8
import httplib
import urllib

data1 = urllib.urlencode({'name':'windard'})
data2 = urllib.urlencode({'admin':'windard','name':'hero'})

conn1 = httplib.HTTPConnection('192.168.137.1')
#发送GET请求,需要自己加上？
conn1.request('GET','/test.php?'+data1)
res1 = conn1.getresponse()
print res1.read()
conn1.close()

conn2 = httplib.HTTPConnection('192.168.137.1')
#发送POST请求
conn2.request('POST','/test.php',data2)
res2 = conn2.getresponse()
print res2.read()

head = res2.getheaders()
for i,j in head:
	print i+"  :  "+j

conn2.close()
