#coding=utf-8
import requests
url = 'http://localhost/upload/1/upload.php'
files = {'file': open('xidian.jpg', 'rb'),}
data  = {'submit':'true'}
#也可以自己设置文件名
#files = {'file': ('xidian.jpg', open('xidian.jpg', 'rb'))}     
page = requests.post(url, data=data,files=files)
html = page.content
print html