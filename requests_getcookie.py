import requests
r = requests.get('http://www.baidu.com')
print r.cookies['BAIDUID']
print r.cookies