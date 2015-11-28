#coding=utf-8
import requests
from requests.auth import HTTPBasicAuth
page = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
# 简写
# page = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    
print page.json()