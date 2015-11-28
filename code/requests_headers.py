import requests
url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.12 Safari/537.36'} 
page = requests.get(url=url,headers=headers)
html = page.content
print html