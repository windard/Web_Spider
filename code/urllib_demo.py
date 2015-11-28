# coding=utf8
#导入urllib库
import urllib
#设定将要请求的URL地址
url = 'http://www.baidu.com'
#其实重点就这一句
page = urllib.urlopen(url)
#读取接收到的数据
html = page.read()
#打印接受到的数据
print html

