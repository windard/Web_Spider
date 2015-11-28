# coding=utf-8
import requests
import urllib
url = 'http://localhost/upload/1/upload.php'
filepath=unicode(r'C:\Users\dell\Desktop\Document\人事处\2011以前年度考核登记表.docx','utf-8')  
files = {'file':(urllib.quote('2011以前年度考核登记表.docx'), open(filepath, 'rb'))}
data  = {'submit':'true'} 
page = requests.post(url, data=data,files=files)
code = page.status_code
html = page.content
if code == 200:
	print "Successful ~"
	print html
else:
	print "Failed ~"