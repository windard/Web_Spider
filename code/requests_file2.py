#coding=utf-8
import requests
url = 'http://localhost/upload/1/upload.php'
data = {'submit':'true'}
#必需自己设定设置文件名
files = {'file': ('test.txt', b'Hello Requests.')}     
page = requests.post(url, data=data,files=files)
html = page.content
print html