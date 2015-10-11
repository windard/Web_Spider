import urllib
url = 'http://localhost/112/images/xidian.jpg'
# pic = urllib.urlretrieve(url,'xidian.jpg')
pic = urllib.urlretrieve(url,url.split('/')[-1])
print pic[0]
print pic[1]