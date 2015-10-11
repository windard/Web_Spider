#coding=utf-8
import requests
from requests.auth import HTTPDigestAuth
page = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPDigestAuth('user', 'pass'))
print page.content