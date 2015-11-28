import urllib
params = urllib.urlencode({'name':'admin','email':'me@wenqiangyang.com'})
page = urllib.urlopen("http://localhost/form_get.php?%s" % params)
html = page.read()
print html