import urllib
params = urllib.urlencode({'name':'windard','email':'me@wenqiangyang.com'})
page = urllib.urlopen("http://localhost/form_post.php",params)
html = page.read()
print html