import urllib2
url = 'http://www.baidu.com'
page = urllib2.urlopen(url)
html = page.read()
print html