#coding=utf-8
import requests
url  = 'http://localhost/112/index.html'
page = requests.get(url)
html = page.content
print html