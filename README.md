# python网络爬虫

##  关于爬虫
网络爬虫，即Web Spider，抓取网页数据，像Google，Baidu等公司，他们的搜索引擎每天都派出数以亿万的爬虫夜以继日的抓取网络数据并存储起来，无数的网络工程师为他们的抓取速度，存储效率做优化。

当然他们的爬虫不是用python写的，不过python强大的各种函数库的使用也可以做简单的爬虫来玩玩。本系列教程博客主要使用的python库有urllib urllib2 request re和cookielib。因为python2.x与python3.x有一定区别，特作强调，本系列博客使用的是在Windows 10下的python2.7.10。

##  urllib

####  基本使用
urllib是几乎所有的python网络爬虫都会使用的库，功能很简单直接，向指定URL发送http请求并接受数据，以下是一个urllib基本实例。 

```python
# coding=utf-8

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
```

保存为urllib_demo.py,运行。如果你得到的是一堆类似于这种的密密麻麻的数据，就说明urllib请求和接收正常。

![BAIDU源码](images/baidu.jpg)

可以看出来urllib库的主要函数就是urlopen()，其实跟基本的文件操作很类似，open打开一个文件，然后用read()读取文件内容，所以也能用readline()来单行读取文件内容。

####  进阶操作

######  发送请求

urlopen的可选参数当然不止一个，比如说或许我们需要在http中同时发送get或者post请求，我们就需要一个参数 params 或者 data ， params 是 get 请求的参数， data 是 post 请求的数据，同时我们还需要一个函数， urlencode ，将我们的参数进行封装。

1. GET请求

在这里我们使用我本地服务器上一个小例子来演示一下，GET请求的页面代码如下，保存在根目录下，命名为form_get.php。

```
<?php 
    $NAME = $_GET['name'];
    $EMAIL = $_GET['email'];
    if($NAME == 'admin'){
        echo "Welcome Back ";
        echo "Your Email : ".$EMAIL;
    }else{
        echo "Get Out !";
    }
?>
```

然后就是我们的python发送get请求：

```
# coding=utf-8

import urllib

params = urllib.urlencode({'name':'admin','email':'me@wenqiangyang.com'})
page = urllib.urlopen("http://localhost/form_get.php?%s" % params)

html = page.read()
print html

```

保存为urllib_get.py,运行，看一下接收回来的数据。

![GET请求](images/get.jpg)

在此处也可以采用另一种的写法：

```

# coding=utf-8

import urllib

url = 'http:localhost/form_get.php'

params = urllib.urlencode({'name':'admin','email':'me@wenqiangyang.com'})
page = urllib.urlopen(url+'?'+params)

html = page.read()
print html

```

仔细分析一下代码就可以看出来%s是将params内的参数直接加到了URL的后面来仿制一个get请求，那么post请求该如何处理呢？post的数据并不在URL上的吖。

2. POST请求

本地服务器上POST请求的页面代码如下，同样保存在根目录下，命名为form_post.php。

```php
<?php 
	$NAME = $_POST['name'];
	$EMAIL = $_POST['email'];

	if($NAME == 'admin'){
		echo "Welcome Back ";
		echo "Your Email : ".$EMAIL;
	}else{
		echo "Get Out !";
	}
?>
```

然后就是我们的python发送post请求：

```python
# coding=utf-8

import urllib

params = urllib.urlencode({'name':'windard','email':'1106911190@qq.com'})
page = urllib.urlopen("http://localhost/form_post.php",params)

html = page.read()
print html

```

保存为urllib_post.py,运行，看一下接收回来的数据。

![POST请求](images/post.jpg)

仔细分析一下源码可以看出来，urlopen的第一个参数已经出现了，就是params可以在发送http请求是附带其他数据或者参数，来实现不同的http请求。
urllib除了可以发送简单get和post请求，还可以发送put和delect请求，这两种比较复杂，这里就不在做详细讲解了。

###### urlopen返回对象

前面已经说到，urlopen的操作与文件的基本操作类似，但是urlopen返回的对象除了基本的读取操作之外还有一些其他的操作。

**urlopen返回对象提供方法：**
- read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
- info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
- getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
- geturl()：返回请求的url

我们来试一下，还是以百度为例：

```python

# coding=utf8

#导入urllib库
import urllib

#设定将要请求的URL地址
url = 'http://www.baidu.com'

#其实重点就这一句
page = urllib.urlopen(url)

#读取接收到的返回信息
info = page.info()

#打印出来
print "Info:"
print info

#读取接收到的返回状态码
code = page.getcode()

#打印出来
print "Code:"
print code

```

保存为urllib_info.py，运行，看一下结果。

![urllib返回值](images/info.jpg)

可以看到http请求返回的信息，还有表示请求成功的200状态码。

###### urllib.urlretrieve

这有一个很实用的函数，它的功能是将URL定位的文件下载到本地，可不仅仅是html哦，这里我们直接给出它相应的需要的参数。

**urllib.urlretrieve(url[,filename[,reporthook[,data]]])**
- url：需要下载的文件的url
- filename：下载了之后保存在本地的名称
- reporthook：执行完了之后的回调函数
- data：跟url传输过去的参数

如果不指定filename，则会存为临时文件。

**urlretrieve()返回一个二元组(filename,mine_hdrs)**
- filename：传入参数的filename，保存在本地的文件名
- mine_hdrs：文件的基本信息


让我们来下载一个本地服务器的照片到python文件所在的文件夹。

照片是这样的：

![服务器上的照片](images/xidian_server.jpg)

python代码如下：

```python

# coding=utf-8
import urllib

url = 'http://localhost/112/images/xidian.jpg'
pic = urllib.urlretrieve(url,'xidian.jpg')

print pic[0]
print pic[1]

```

保存为urllib_urlretrieve.py,运行，看一下结果。

![urlretrieve结果](images/urlretrieve.jpg)

确实是返回文件名和文件信息，看一下文件夹，也保存下来了xidian.jpg这个照片。
这里有一个小技巧，就是文件名的设定。
我不是指定文件名了么，在url里面，不想早后面再自己手动的写文件名了，就可以这样写：

```
pic = urllib.urlretrieve(url,url.split('/')[-1])
```

将URL按 `/` 截断，取最后一个字符串，即是我们想要的文件名。

#### urllib其他函数

- urllib.urlcleanup

前面说到urllib.urlretrieve()下载指定url的文件如果不指定保存文件名的话就会存为临时文件，在缓存里，那么这个函数就是清除这里产生的缓存。

- urllib.quote(url)和urllib.quote_plus(url)

将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受，简单的看一下效果。

```
>>>import urllib
>>> urllib.quote('http://www.baidu.com')
'http%3A//www.baidu.com'
>>> urllib.quote_plus('http://www.baidu.com')
'http%3A%2F%2Fwww.baidu.com'
```

- urllib.unquote(url)和urllib.unquote_plus(url)

与上一个函数功能相反，将编码后的url还原。

那么到这里我们的urllib函数就讲完了，是不是功能很强大呢？别担心，还有更强大的呢~

## urllib2

#### 基本使用

urllib2作为urllib的升级版，基本功能和使用是和urllib一致的，也可以用urlopen来发送一个请求，如下所示：

```python
# coding=utf-8

import urllib2

url = 'http://www.baidu.com'
page = urllib2.urlopen(url)

html = page.read()

print html
```

保存为urllib2_demo.py,运行，看一下结果。

![urllib2_baidu_HTML](images/urllib2_baidu.jpg)

可以看到跟urllib的基本写法一致，返回结果也一致。

但是这只是看起来一致而已，如果我们去翻看官方手册的话就会看到其实它们的参数有一定的不同。

`urllib.urlopen(url[,data[,proxies]])` 和 `urllib2.urlopen (url [,data [,timeout]])` 虽然前两个参数都是http请求地址URL和传输的数据data，但是第三个参数由没什么用的proxies换为了超时时间timeout，即在中断连接前尝试的时间，这样的话可以设定http请求如果超过多长时间就放弃，避免长时间的等待，浪费网络资源。

#### 进阶操作

###### urllib2.Request

既然urllib2是urllib的升级版，那么它肯定有不同于urllib的地方，那就是它引入了一个新的函数Request()，让我们来看一下Request()的使用。

它的功能是将你的http请求更加实例化，让http请求更加饱满，伪装成一个真正的浏览器发送的请求。因为有的站点为了避免被恶意的网络爬虫抓取，会对发送过来的http请求做一定的删选。

```python

#coding=utf-8

import urllib2
url = 'http://www.baidu.com'

#加入http请求的请求者地址，此处是本人的chrome 45.0.2454.12
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.12 Safari/537.36'

#封装成http请求头
headers = {'User-Agent':user_agent}

#将http请求头加入到Request中，组装成一个完整的请求
req = urllib2.Request(url=url,headers=headers)

#此时urlopen就不再是直接请求URL了，而是请求已经封装好了的Req对象
page = urllib2.urlopen(req)

html = page.read()
print html
```

保存为urllib2_request.py，运行，看一下结果。

![urllib2_baidu_HTML2](images/urllib2_baidu2.jpg)

显得并没有什么区别，当然没有什么区别，百度对headers并不敏感，但是起码说明这个语法是正确的，那么接下来就让我们来看一下这个函数到底有哪些参数。
（当然在headers里面也远不仅仅只有User-Agent这一个参数，但这个参数是必选参数，当然也还有一些其他的参数，比如说content-type。）

**Request (url [data,headers [,origin_req_host ,[unverifiable]]]])**
- URL：统一资源定位符，即http请求的网址
- data：请求过程中传输的数据，用于POST请求
- header：http请求头
- origin_req_host：原始请求地址
- unverifiable：不知道是什么东西的东西

一般常用到的是前三个，现在我们用urllib2来重新实现一个post请求，还是请求本地服务器环境的form_post.php。

```python
# coding=utf-8

import urllib2
import urllib

url = 'http://localhost/form_post.php'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.12 Safari/537.36'

value = {'name':'admin','email':'me@wenqiangyang.com'}
data  = urllib.urlencode(value)
headers = {'User-Agent':user_agent}

req = urllib2.Request(url, data, headers)
page = urllib2.urlopen(req)

html = page.read()
print html
```

保存为urllib2_post.py，运行，看一下结果。

![urllib2_POST](images/urllib2_post.jpg)

确实可以发送一个带着http请求头的post请求，虽然看不出来与之前有什么区别。
那么既然可以发送post请求，那么用之前的第二种方法发送get请求当然也可以，这里就不再做演示了。

###### urllib2.build_opener

基本的urlopen()函数不支持验证、cookie或其他HTTP高级功能。要支持这些功能，必须使用 `urllib2.build_opener()` 函数来创建自己的自定义Opener对象。

在使用 cookie 时是配合 cookielib 一起使用，我们来试一下使用 build_opener 登陆 HTTPBasicAuthentication ，和使用 build_opener 设置代理 和使用 build_opener 连接 FTP 服务器上传下载文件。

首先我们来试一下 HTTPBasicAuthentication ，这次我们自己搭建一个 HTTP Basic Authentication 页面，使用 Python Flask。

```
from functools import wraps
from flask import request, Response

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})   

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/secret-page')
@requires_auth
def secret_page():
    return "Auth Successful ~"

if __name__ == '__main__':
    app.run()
```

我们直接在浏览器查看认证页面是这样的。

![http_basic_auth](images/http_basic_auth.png)

现在我们试着用 urllib2 来做 HTTP Basic 身份认证。

```
# coding=utf-8

import urllib2

try:
	f = urllib2.urlopen('http://127.0.0.1:5000/secret-page')
except Exception,e:
	print e

# set up authentication info
authinfo = urllib2.HTTPBasicAuthHandler()
authinfo.add_password(realm="Login Required", uri="http://127.0.0.1:5000/secret-page", user='admin', passwd='secret')

# build a new opener that adds authentication and caching FTP handlers
opener = urllib2.build_opener(authinfo)

# install it
urllib2.install_opener(opener)

f = urllib2.urlopen('http://127.0.0.1:5000/secret-page')

print f.read()
```

![urllib2_basic_auth](images/urllib2_basic_auth.png)

然后我们试一下代理能不能用

```
# coding=utf-8

import urllib2

f = urllib2.urlopen('http://members.3322.org/dyndns/getip')
print f.read()

proxy_support = urllib2.ProxyHandler({"http" : "http://124.88.67.17:843"})
opener = urllib2.build_opener(proxy_support)

# install it
urllib2.install_opener(opener)

f = urllib2.urlopen('http://members.3322.org/dyndns/getip')
print f.read()

```

![urllib2_proxy](images/urllib2_proxy.png)

如果代理需要身份验证的话可以使用 `http://user:pass@124.88.67.17:843` 来进行身份验证。

最后我们试一下登陆 FTP 服务器并下载一个文件操作。

FTP 服务器

```
# coding=utf-8

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("admin", "password", "D:\\", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
```

使用 Python 登陆并下载文件

```
# coding=utf-8

import urllib
import urllib2

f = urllib2.urlopen('ftp://admin:password@127.0.0.1/test.txt')

print f.read()

urllib.urlretrieve('ftp://admin:password@127.0.0.1/test.txt', 'test.txt')

print "Download successful ~"
```

![urllib2_ftp](images/urllib2_ftp.png)

#### urllib与urllib2的区别

urllib与urllib2还是有一定的区别的，除了我们前面所说的urlopen的参数不一样之外，因为这些区别，使urllib和urllib2同样重要，两者配合使用，才能发挥更大威力。

- urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL。这意味着，你不可以通过urllib模块伪装你的User Agent字符串等（伪装浏览器）。
- urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。所以urllib2发送GET请求或者POST请求都需要urllib的帮助，这也是为何urllib常和urllib2一起使用的原因。
- urllib2模块比较优势的地方是urlliburllib2.urlopen可以接受Request对象作为参数，从而可以控制HTTP Request的header部。
- 但是urllib.urlretrieve函数以及urllib.quote等一系列quote和unquote功能没有被加入urllib2中，因此有时也需要urllib的辅助。

## requests

#### 安装

- 通过pip或者easy_install安装

```
$ pip install requests
```

或者

```
$ easy_install requests
```

- 下载代码后安装

```
$ git clone git://github.com/kennethreitz/requests.git
$ cd requests
$ python setup.py install
```

- 通过IDE安装吧，如 pycharm

#### 基本使用

requests库是基于urllib的，但是它比urllib更方便，更强大，让我们看一下它的基本使用：

```python

#coding=utf-8

import requests

url  = 'http://localhost/112/index.html'
page = requests.get(url)

html = page.content

print html
```

跟urllib一样的简洁而又强大，短短的几行代码就可以构造一个http请求。

#### 进阶操作

###### requests发送请求

但是它和urllib又有不同之处，urllib默认的是发送get请求，但是requests需要指定发送哪种请求，看似更加复杂，但是其实让我们获得更多的选择更便利。requests支持GET/POST/PUT/DELETE/HEAD/OPTIONS等请求类型，它们的使用也非常方便。

```python
>>> r = requests.get("http://httpbin.org/get")
>>> r = requests.post("http://httpbin.org/post")
>>> r = requests.put("http://httpbin.org/put")
>>> r = requests.delete("http://httpbin.org/delete")
>>> r = requests.head("http://httpbin.org/get")
>>> r = requests.options("http://httpbin.org/get")
```

> KISS -- Keep　It　Simple  Stupid <br>
> 一切本该如此简单

那么既然可以发送GET或者POST请求，那它们的参数在哪里呢？
就在requests()的第二个和第三个参数，第二个参数params，第三个参数data，分别用来接收get和post的数据。
我们还是来试一下发送请求给本地服务器看一下结果怎么样，还是form_get.php和form_post.php。

```python
# coding=utf-8

import requests

get_url  = 'http://localhost/form_get.php'

get_params = {'name':'admin','email':'me@wenqiangyang.com'}
post_url = 'http://localhost/form_post.php'

post_params = {'name':'windard','email':'1106911190@qq.com'}

get  = requests.get(url=get_url,params=get_params)
post = requests.post(url=post_url,data=post_params)

get_html = get.content
post_html = post.content

print get_html
print post_html
```

保存为requests.request.py,运行，看一下结果。

![requests_request](images/requests_request.jpg)

确实都能够成功的发送相应的请求。

requests除了能够更方便的发送请求之外，还将urllib里面的复杂的操作简化了很多。
上面的例子可以看出来get或者post请求时发送的数据不需要再经过打包就可以直接发送，其实像这样的简化还有不少，比如说headers。

```python
# coding=utf-8

import requests

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.12 Safari/537.36'} 

page = requests.get(url=url,headers=headers)
html = page.content

print html

```

保存为requests_headers.py,运行，看一下结果。

![requests_headers](images/requests_headers.jpg)

可以看出来，还是结果没什么变化，但是它的语法规则比urllib更简洁了不少。
在这里，不但可以设定请求头，也可以作为查看请求头来使用，例如`page.requests.headers`就可以查看请求头。

###### requests上传文件

使用 Requests 模块，上传文件也是如此简单的，文件的类型会自动进行处理。

我们来试一下用post方法向我本地服务器上传一张照片。

服务器上的php代码如下。

```
<?php
error_reporting(0);
if(isset($_POST['submit'])){
	$upfile = $_FILES['file']['name'];
	$filename =strstr($upfile, '.', true);
	if (file_exists("upload/" . $_FILES["file"]["name"]))
    {
		echo $_FILES["file"]["name"] . " already exists. ";
    }
    else
    {
		move_uploaded_file($_FILES["file"]["tmp_name"],"upload/" . $_FILES["file"]["name"]);
		echo "Stored in: " . "upload/" . $_FILES["file"]["name"];
    }
}else{

		die('Upload failed..');
}
?>
```

保存在`http://localhost/upload/1/upload.php`,接下来是python代码。

```python
# coding=utf-8

import requests

url = 'http://localhost/upload/1/upload.php'

files = {'file': open('xidian.jpg', 'rb'),}
data  = {'submit':'true'}

#也可以自己设置文件名
#files = {'file': ('xidian.jpg', open('xidian.jpg', 'rb'))}

page = requests.post(url, data=data,files=files)

html = page.content
print html

```

保存为requests_file.py,运行，看一下结果。

![requests_file](images/requests_file.jpg)

上传成功，而且更加方便的是，你可以把字符串当着文件进行上传，就是自己边创建文件边上传，如下所示。

```python
# coding=utf-8

import requests
url = 'http://localhost/upload/1/upload.php'

data = {'submit':'true'}

#必须自己设定设置文件名
files = {'file': ('test.txt', b'Hello Requests.')}     

page = requests.post(url, data=data,files=files)

html = page.content
print html
```

保存为requests_file2.py,运行，看一下结果。

![requests_file2](images/requests_file2.jpg)


>*2015-10-17更新*

今天用到了这个上传文件的操作，加深了印象。

主要是关于含有中文字符的文件上传，虽然我一直在电脑上避免使用含有中文的文件，但是总是避免不了在某些地方要使用到中文字符。

可是在http协议中是不支持中文的，也就是在http请求中的中get或者post传输的数据是不能有中文的，这一点就很坑爹了。

解决办法就是在传输过去的时候将中文数据进行URLencode，然后在服务器接受的那边将收到的数据再用URLdecode。

Python的URLencode用的是urllib的urlencode()函数，但是这个函数是将json格式的数据编码的，单个数据用的是quote()。以前还不觉得将数据编码有什么用，现在知道了有重大作用。

php直接使用urldecode将编码后的数据解码。php的编码函数有urlencode()和rawurlencode()。

这两个函数的区别是urlencode 将空格则编码为加号 `+`，rawurlencode 将空格则编码为 `%20`。

在上传文件的时候，因为还需要将文件按二进制打开，所以还涉及到二进制打开文件的操作，这里就不详细讲解了，可以参看我的另一篇博客。

```python

# coding=utf-8

import requests
import urllib

url = 'http://localhost/upload/1/upload.php'
filepath = unicode(r'C:\Users\dell\Desktop\Document\人事处\2011以前年度考核登记表.docx','utf-8')  
files = {'file':(urllib.quote(u'2011以前年度考核登记表.docx'), open(filepath, 'rb'))}

data  = {'submit':'true'}
page = requests.post(url, data=data,files=files)
code = page.status_code
html = page.content
if code == 200:
	print "Successful ~"
	print html
else:
	print "Failed ~"

```

保存为requests_file3.py

###### requests其他功能

- 身份验证
 1. 基本身份认证(HTTP Basic Auth)

```python

#coding=utf-8

import requests

from requests.auth import HTTPBasicAuth
page = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))

# 简写
# page = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    

print page.json()

```

保存为requests_basicauth.py,运行，看一下结果。

![requests_basicauth](images/requests_basicauth.jpg)

 2. 摘要式身份认证(HTTP Digest Auth)

写法与上类似 `requests.get(URL, auth=HTTPDigestAuth('user', 'pass'))` 不再做详细阐述。

- cookies与session
 - 获得cookies。比如说我们在访问Baidu时，它就会自动的给我们设定一个cookies，现在让我们来看一下这些cookies。

```python
# coding=utf-8

import requests

r = requests.get('http://www.baidu.com')
print r.cookies['BAIDUID']

print r.cookies
```

保存为requests_getcookie.py,运行，看一下结果。

![requests_getcookie](images/requests_getcookie.jpg)

可以看出来一连串的cookies，那么这些是服务器给我们设定的cookies，如果服务器需要我们向它发送cookies的话要怎么办呢？
 
 - 发送cookies。比如说很多网站都有保存密码的功能，就是在你每次访问站点是先检查你本机的cookies，cookies里面存储了你的账户名和密码，如果你的cooki
 es存在且正确，就可以直接登录，不再需要输入账户名和密码。

在这里我们访问我本地服务器上的一个页面，代码如下，

```php
<?php 
	$COOKIE = $_COOKIE['name'];
	if(isset($COOKIE)){
		if($COOKIE == 'admin'){
			echo "Welcome Back";
		}else{
			echo "Get Out!";
		}
	}
 ?>
```

保存在根目录下，命名为cookies.php。python代码如下。

```python
# coding=utf-8

import requests

url = 'http://localhost/cookies.php'
cookies = {'name': 'admin', 'email': 'me@wenqiangyang.com'}

page = requests.get(url, cookies=cookies)

html = page.content
print html
```

保存为requests_setcookie.py，运行，看一下结果。

![requests_setcookie](images/requests_setcookie.jpg)

除了cookies之外，还有session，不过这个session可不是保存在服务器端的那个session，那个session是服务器设定的保存在服务器端的我们也没有办法更改，此处的session是指我们在与某个URL通信发送http请求时，保持会话，让同一个cookies长期有效，因为有可能你需要发送不止一次的http请求，又不想每次发送请求的时候都带上cookies。同一个Session实例发出的所有请求之间保持cookies，且这些都是自动处理的，甚是方便。

- timeout超时

timeout就是连接超时，设定连接时间，如果超过多久就自动放弃并报错，节省网络资源。

```python
>>>import requests
>>>page = requests.get('http://www.github.com',timeout=0.01)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
```

肯定会报错嘛，时间太短了，只是看一看timeout的功能。

- requests其他参数
 - allow_redirects：是否禁止跳转。有的网站设定了302重定向，这样的话，我们的请求在遇到这个重定向是会自动跳转的，而且返回状态码也是200，比如说`http://www.baidu.com`，其实在2015年上半年，百度已经做了全站https，也就是说你在访问`http://www.baidu.com`，它是有一个重定向自动的给你跳转到`https://www.baidu.com`的，但是如果设定`allow_redirects=False`，就不会发生跳转，返回状态码302。
 - proxies：设定代理。有时为了避免直接请求别人的站点，通常会设置代理，或者采集时为避免被封IP，也经常会使用代理。那就只需要这样。

```python
# coding=utf-8

import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("http://www.zhidaow.com", proxies=proxies)

```

如果代理需要账户和密码，则需这样：

```python
proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}
```

 - verify：Requests可以为HTTPS请求验证SSL证书，就像web浏览器一样。要想检查某个主机的SSL证书，你可以使用 verify 参数。当使用requests.get(url)抓取HTTPS网页时，会遇到requests.exceptions.SSLError错误，可能是因为该网页SSL证书失效，这时需要将verify设置为False即可。默认为True。


###### requests返回对象

在urllib里我们曾说道urlopen的返回对象是与文件打开的对象类似，但是requests返回对象可不是这样，所以如果想查看返回内容，不能使用read()函数，而是使用content函数，或者在python3.X里使用text函数，就像这样`print(page.text)`，除了返回页面内容之外，还有一些其他的内容。

- status_code：响应状态码
- encoding：查看编码信息，使用自定义的编码进行解码
- raw：返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
- content：字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
- text：字符串方式的响应体，会自动根据响应头部的字符编码进行解码
- headers：以字典对象存储服务器响应头。（但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None）
- json()：Requests中内置的JSON解码器，解析读取json
- raise_for_status()：失败请求(非200响应)抛出异常
- history：查看是否有重定向，取得重定向的URL。

让我们来试一下。

```python
# coding=utf-8

import requests

url = 'http://www.baidu.com'

page = requests.get(url=url)

code = page.status_code
headers = page.headers

print code
print headers

```

保存为requests_info.py,运行，看一下结果。

![requests_info](images/requests_info.jpg)

好吧，运行结果是正常的，就是headers那里是直接输出了，没有urlopen返回对象用info()解析的那么好看，没事，我们自己来排版一下就可以。

```python
# coding=utf-8

import requests

url = 'http://www.baidu.com'
page = requests.get(url=url)

code = page.status_code
headers = page.headers

print code

for key,value in headers.items():
	print key+' : '+value
```

保存为requests_info2.py,运行，看一下结果。

![requests_info2](images/requests_info2.jpg)

这下好看多了，结果显示也是和urlopen返回对象的info()的结果类似。


## re

re库是Python的正则表达式，基本用法与其他语言的正则表达式使用基本一致，当然也有一定的自己语言的东西。         
基础的语法说明就不讲了，都是一致的。    

1. re.compile(strPattern[,flag])  将字符串形式的正则表达式编译成Pattern对象，第二个参数是匹配模式。    

>匹配模式有： <br>
>re.I :忽略大小写 <br>
>re.M :多行模式，可以改变`^`和`$`的行为 <br>
>re.S :点任意匹配模式，改变`.`的行为 <br>
>re.L :使预定字符类 \w \W \b \B \s \S 取决于当前区域设定 <br>
>re.U :使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性 <br>
>re.X :详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释 <br>

详细的一篇在 [这里](https://github.com/windard/Python_Lib/tree/master/content/re.md)

[Python正则表达式指南](http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)

## cookiesjar

因为 urllib 和 urllib2 库都不能方便的设置 cookies ，一般是与 cookiesjar 配合使用来设置保存使用 cookies

### 获得 cookies

```
# coding=utf-8

import urllib2
import cookielib

cookie = cookielib.CookieJar()
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)

opener.open("https://www.baidu.com")

# print cookie

for item in cookie:
	print item.name, ":", item.value
```

### 更改 cookies

比如说这样的一个站，`cookies.php`

```
<?php 

if (isset($_COOKIE['user']) && $_COOKIE['user'] == 'admin'){
	echo "Welcome Aadmin";
}else{
	echo $_COOKIE['user'];
	echo "Welcome Guest";
	setcookie("user","guest");
}
 ?>
```

可以这样伪装自己

```
# coding=utf-8

import urllib2
import cookielib

cookie = cookielib.CookieJar()
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)

result = opener.open("http://127.0.0.1/cookies.php")

print result.read()

for item in cookie:
	print item.name, ":", item.value

# 清除之前的 cookies
cookie.clear()

# 新建一个新的我们的 cookies
c = cookielib.Cookie(version=0, name='user', value='admin', port=None, port_specified=False, domain='127.0.0.1', domain_specified=False, domain_initial_dot=False, path='/', path_specified=False, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)

# 将新的 cookies 添加到 CookieJar 中
cookie.set_cookie(c)

result = opener.open("http://127.0.0.1/cookies.php")

print result.read()
```

![cookies_admin](images/cookies_admin.png)

这样确实就可以成功的设定 cookies 登陆，但是这样自己设定 cookies 太麻烦了，一般使用 cookies 的话都是先正常登陆一个网站然后将 cookies 保存成文本，下次就可以直接使用。

### 保存 cookies

有一个简单的登陆框的站

```
<?php 
	if(isset($_COOKIE['username'])){
		echo "Welcome ".$_COOKIE['username']." Again.";
	}else{
		if(isset($_POST['submit'])){
			$username = $_POST['username'];
			$password = $_POST['password'];
			if($password == 'password'){
				setcookie('username', $username);
				header("Location:login.php");
			}
		}else{
			echo "<form action=\"\" method=\"post\" accept-charset=\"utf-8\">";
			echo "<input type=\"text\" name=\"username\" value=\"\">";
			echo "<br>";
			echo "<input type=\"text\" name=\"password\" value=\"\" >";
			echo "<br>";
			echo "<input type=\"submit\" name=\"submit\" value=\"submit\">";
			echo "</form>";
		}
	}
 ?>
```

```
# coding=utf-8

import urllib
import urllib2
import cookielib

# 使用 MozillaCookieJar 来保存 cookies
cookie = cookielib.MozillaCookieJar("cookies.txt")

handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)

result = opener.open("http://127.0.0.1/login.php")

print result.read()

postdata = urllib.urlencode({
	'username':'中国人',
	'password':'password',
	'submit':'submit'
	})

print postdata

result = opener.open("http://127.0.0.1/login.php", postdata)

print result.read()

# 保存 cookies
cookie.save(ignore_discard=True, ignore_expires=True)

# 再次访问

result = opener.open("http://127.0.0.1/login.php")

print result.read()

# 打印 cookies

for item in cookie:
	print item.name, ":", item.value
```

在 Windows 下的 cmd 中不能正常显示 utf-8 编码的字符集，可以先使用 `chcp 65001` 然后就可以正常显示。

![cookies_login](images/cookies_login.png)


### 使用保存的 cookies

```
# coding=utf-8

import urllib
import urllib2
import cookielib

# 使用刚才已保存的 cookies.txt
cookie = cookielib.MozillaCookieJar()

cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)

handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)

# 打印 cookies

for item in cookie:
	print item.name, ":", item.value

result = opener.open("http://127.0.0.1/login.php")

print result.read()

# 再次登录

data={
    "username":"windard",
    "password":"password",
    "submit":"submit"
}

postdata = urllib.urlencode(data)

headers ={
    "Host":"127.0.0.1", 
    "Referer":"http://127.0.0.1/login.php",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}

req = urllib2.Request("http://127.0.0.1/login.php", postdata, headers)

cookie.clear()

result = opener.open(req)

result = opener.open("http://127.0.0.1/login.php")

print result.read()

```

![cookies_load](images/cookies_load.png)


还有几个部分 beautifulsoup lxml cookiesjar

## httplib

httplib是一个非常底层的http库，像 urllib，urllib2，requests 等，都是将它进行封装之后得到的。                         

这个函数只有两个原型，分别用于 http 和 https 。                

### httplib.HTTPConnection            

这个函数类用来创建一个 http 类型的请求链接，返回一个 HTTPConnection 实例。    

原型：                                                

HTTPConnection(host[, port[, strict[, timeout]]])                   
- host    : 请求的服务器host,不能带http://开头                           
- port    : 请求的服务器端口号，默认是80端口，可以不写                     
- strict  : 是否严格检查请求的状态行，就是http1.0/1.1 协议版本的那一行，即请求的第一行，默认为False，为True时检查错误会抛异常           
- timeout : 单次请求的超时时间，默认为10ms            
                 
### httplib.HTTPSConnection                        

这个函数类用来创建一个 https 类型的请求链接，返回一个 HTTPSConnection 实例。     

原型：                                        

HTTPSConnection(host[, port[, key_file[, cert_file[, strict[, timeout]]]]])
- host    : 请求的服务器host,不能带http://开头                           
- port    : 请求的服务器端口号，默认是80端口，可以不写                     
- key_file   : 一个包含 PEM 格式的公钥文件                                      
- cert_file  : 一个包含 PEM 格式的认证文件                       
- strict  : 是否严格检查请求的状态行，就是http1.0/1.1 协议版本的那一行，即请求的第一行，默认为False，为True时检查错误会抛异常           
- timeout : 单次请求的超时时间，默认为10ms                       

#### HTTPConnection.request

发送一个请求。无返回值，自身对象发生一定的转化。                    

原型:                                

HTTPConnection.request(method, url[, body[, headers]])                      
- method    : 请求的方式，如'GET','POST','HEAD','PUT','DELETE'等
- url       : 请求的网页路径，相对于根目录的相对路径            
- body	    : 请求是否带数据，如POST请求的参数，参数需要经过编码          
- headers   : 请求是否带请求头信息，该参数是一个字典，不过键的值是指定的http头关键字                                     

#### HTTPConnection.putheader

设定请求头的内容

原型：

HTTPResponse.putheader(header, *values)
- header 	: 请求头的键
- values    : 请求头的值

#### HTTPConnection.getresponse

取得一个http相应对象，返回 HTTPResponse 实例                       

#### HTTPConnection.close                              

关闭HTTPConnection链接，无返回值，自身对象发生一定的转化。            

#### HTTPConnection.connect      

开启HTTPConnection链接，无返回值，自身对象发生一定的转化。              

#### HTTPConnection.send      

发送 POST 请求的数据，无返回值，自身对象发生一定的转化。              

#### HTTPResponse.read

获得http响应的内容部分，即网页源码,返回字符串。                        

原型：                             

res.read([amt])                  
- amt    : 读取指定长度的字符，默认为空，即读取所有的内容。          

#### HTTPResponse.getheaders                  

获得所有的响应头内容，返回一个元祖列表。                                    

#### HTTPResponse.getheader

获得指定的响应头内容                         

原型：                          

res.getheader(name[,default])                    
- name      : 响应头的键值                   
- default   : 若没有找到前一个响应头，则默认查找这个响应头                   

#### HTTPResponse.msg 属性                          

所有的响应头信息，和getheaders()方法一样，不过这个返回的是原始字符串     

#### HTTPResponse.status 属性

这次请求的返回状态码                                             

#### HTTPResponse.version 属性

这次请求的http协议版本 ,10表示http/1.0 ,11表示http/1.1                  

#### HTTPResponse.reason 属性                                

这次请求的的状态的表述内容，200 是 OK, 404 是 Not Found        

```python
# coding=utf-8

import httplib

#建立一个HTTPConnection对象
conn1 = httplib.HTTPConnection('192.168.137.1')

#发送GET请求
conn1.request('GET','/test.php')

#得到一个HTTPResponse对象
res1 = conn1.getresponse()

#打印页面内容
print res1.read()

#得到返回响应头
head = res1.getheaders()

#打印返回响应头
for i,j in head:
	print i+"  :  "+j

#打印返回对象的msg属性
print res1.msg

#打印返回对象的状态码
print res1.status

#打印返回对象的version
print res1.version

#打印返回对象的reason
print res1.reason

conn1.close()
```

保存为httplib_demo.py，运行，看一下结果。

![httplib_demo.png](images/httplib_demo.png)

再来一个发送GET请求和POST请求的http连接。         

```python
#coding=utf-8

import httplib
import urllib

conn2 = httplib.HTTPConnection('192.168.137.1')

data1 = urllib.urlencode({'name':'windard'})
data2 = urllib.urlencode({'admin':'windard'})

#发送GET请求,需要自己加上
conn2.request('GET','/test.php?'+data1)

res1 = conn2.getresponse()
print res1.read()

#发送POST请求
conn2.request('POST','/test.php',data2)

res2 = conn2.getresponse()
print res2.read()

head = res2.getheaders()
for i,j in head:
	print i+"  :  "+j

conn2.close()
```

保存为httplib\_post.py，运行，看一下结果。          

![httplib_post.png](images/httplib_post.png)               


网上还有很多相关的教程博客

[Python 3开发网络爬虫(二)](http://www.yiibai.com/python/python3-webbug-series2.html) <br>
[Python 3.x爬虫技巧总结](http://blog.csdn.net/wangtaoking1/article/details/18308635) <br>
[ 端口扫描工具python-nmap的使用](http://blog.csdn.net/wangtaoking1/article/details/9620967) <br>
[ Python正则表达式指南](http://blog.csdn.net/wanghuiqi2008/article/details/8078084) <br>
[用python的BeautifulSoup分析html](http://www.cnblogs.com/twinsclover/archive/2012/04/26/2471704.html) <br>
[Python爬虫入门八之Beautiful Soup的用法](http://cuiqingcai.com/1319.html) <br>
[Python中Cookie的处理（一）Cookie库](http://www.cnblogs.com/linxiyue/p/3536935.html) <br>
[Python中Cookie的处理（二）cookielib库](http://www.cnblogs.com/linxiyue/p/3536960.html) <br>
[逝去日子的博客](http://www.lylinux.org/%E4%BD%BF%E7%94%A8python%E6%89%93%E5%BC%80%E5%9B%BE%E7%89%87.html) <br>
[Python标准库之urllib，urllib2](http://www.cnblogs.com/linxiyue/p/3537486.html) <br>
[Python标准库之urllib，urllib2自定义Opener](http://www.cnblogs.com/linxiyue/p/3537557.html) <br>
[python学习之re模块](http://zipperary.com/2013/07/29/python-re/) <br>
[python学习之yield](http://zipperary.com/2013/07/30/python-yield/) <br>
[深入理解urllib、urllib2及requests](http://www.codefrom.com/paper/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3urllib%E3%80%81urllib2%E5%8F%8Arequests) <br>
[urllib与urllib2的学习总结(python2.7.X)](http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html) <br>
[Python爬虫入门五之URLError异常处理](http://cuiqingcai.com/961.html) <br>
[Python爬虫入门六之Cookie的使用](http://cuiqingcai.com/968.html) <br>
[urllib2 的使用细节转](http://www.lxway.net/25118564.html) <br>
[Python 标准库 urllib2 的使用细节](http://zhuoqiang.me/python-urllib2-usage.html#redirect) <br>
[黄聪：使用Python中的HTMLParser、cookielib抓取和解析网页、从HTML文档中提取链接、图像、文本、Cookies（二）](http://www.cnblogs.com/huangcong/archive/2011/08/31/2160747.html) <br>
[Python使用cookielib和urllib2模拟登陆新浪微博并抓取数据](http://www.crazyant.net/796.html) <br>
[模拟登录新浪微博（Python)](http://www.douban.com/note/201767245/) <br>
[urllib2模块](http://www.cnblogs.com/mmix2009/p/3226775.html) <br>
[cookielib和urllib2模块相结合模拟网站登录](http://www.cnblogs.com/sysu-blackbear/p/3629770.html) <br>
[Python Urllib2和Cookielib的综合使用](http://www.cnblogs.com/abcat/p/3702349.html) <br>
[python中的cookielib的使用方法](http://www.phpgao.com/python-cookielib.html) <br>
[](http://candychen.gift/index.php/archives/10/) <br>
[用Python模拟浏览器登录](http://zipperary.com/2013/08/16/python-login/) <br>


## 参考链接

[Python核心模块——urllib模块](http://www.cnblogs.com/sysu-blackbear/p/3629420.html)

[urllib模块和urllib2模块的区别](http://www.cnblogs.com/sysu-blackbear/p/3630178.html)

[Python 第三方 http 库-Requests 学习](http://www.itwhy.org/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/python/python-%E7%AC%AC%E4%B8%89%E6%96%B9-http-%E5%BA%93-requests-%E5%AD%A6%E4%B9%A0.html)

[python requests的安装与简单运用](http://www.zhidaow.com/post/python-requests-install-and-brief-introduction)

[requests官方文档-安装](http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/install.html#install)

[requests官方文档-快速上手](http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/quickstart.html)

[requests官方文档-高级用法](http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/quickstart.html)

[python--httplib模块使用 ](http://blog.csdn.net/five3/article/details/7078951)















  
