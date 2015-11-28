import requests
url = 'http://localhost/cookies.php'
cookies = {'name': 'admin', 'email': 'me@wenqiangyang.com'}
page = requests.get(url, cookies=cookies)
html = page.content
print html