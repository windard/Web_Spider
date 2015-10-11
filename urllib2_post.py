import urllib2
import urllib
url = 'http://localhost/form_post.php'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.12 Safari/537.36'
value = {'name':'admin','email':'me@wenqiangyang.com'}
data  = urllib.urlencode(value)
headers = {'User-Agent':user_agent}
req = urllib2.Request(url,data,headers)
page = urllib2.urlopen(req)
html = page.read()
print html