#python网络爬虫

---
[TOC]


##关于爬虫
网络爬虫，即Web Spider，抓取网页数据，像Google，Baidu等公司，他们的搜索引擎每天都派出数以亿万的爬虫夜以继日的抓取网络数据并存储起来，无数的网络工程师为他们的抓取速度，存储效率做优化。

当然他们的爬虫不是用python写的，不过python强大的各种函数库的使用也可以做简单的爬虫来玩玩。本系列教程博客主要使用的python库有urllib urllib2 request re和cookielib。因为python2.x与python3.x有一定区别，特作强调，本系列博客使用的是在Windows 10下的python2.7.10。

##urllib

####基本使用
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
![BAIDU源码](baidu.jpg)

可以看出来urllib库的主要函数就是urlopen()，其实跟基本的文件操作很类似，open打开一个文件，然后用read()读取文件内容，所以也能用readline()来单行读取文件内容。

####进阶操作

######发送请求
urlopen的可选参数当然不止一个，比如说或许我们需要在http中同时发送get或者post请求，我们就需要一个参数params或者data，params是get请求的参数，data是post请求的数据，同时我们还需要一个函数，urlencode，将我们的参数进行封装。

1. GET请求
在这里我们使用我本地服务器上一个小例子来演示一下，GET请求的页面代码如下，保存在根目录下，命名为form_get.php。

```php
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
```python
import urllib
params = urllib.urlencode({'name':'admin','email':'me@wenqiangyang.com'})
page = urllib.urlopen("http://localhost/form_get.php?%s" % params)
html = page.read()
print html
```
保存为urllib_get.py,运行，看一下接收回来的数据。
![GET请求](get.jpg)

在此处也可以采用另一种的写法：
```python
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
import urllib
params = urllib.urlencode({'name':'windard','email':'1106911190@qq.com'})
page = urllib.urlopen("http://localhost/form_post.php",params)
html = page.read()
print html
```
保存为urllib_post.py,运行，看一下接收回来的数据。

![POST请求](post.jpg)
仔细分析一下源码可以看出来，urlopen的第一个参数已经出现了，就是params可以在发送http请求是附带其他数据或者参数，来实现不同的http请求。
urllib除了可以发送简单get和post请求，还可以发送put和delect请求，这两种比较复杂，这里就不在做详细讲解了。

######urlopen返回对象的其他操作
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
![urllib返回值](info.jpg)
可以看到http请求返回的信息，还有表示请求成功的200状态码。

######urllib.urlretrieve()
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
![服务器上的照片](xidian_server.jpg)
python代码如下：
```python
import urllib
url = 'http://localhost/112/images/xidian.jpg'
pic = urllib.urlretrieve(url,'xidian.jpg')
print pic[0]
print pic[1]
```
保存为urllib_urlretrieve.py,运行，看一下结果。
![urlretrieve结果](urlretrieve.jpg)

确实是返回文件名和文件信息，看一下文件夹，也保存下来了xidian.jpg这个照片。
这里有一个小技巧，就是文件名的设定。
我不是指定文件名了么，在url里面，不想早后面再自己手动的写文件名了，就可以这样写：
```
pic = urllib.urlretrieve(url,url.split('/')[-1])
```
将URL按'\'截断，取最后一个字符串，即是我们想要的文件名。

####urllib其他函数
1. urllib.urlcleanup()
前面说到urllib.urlretrieve()下载指定url的文件如果不指定保存文件名的话就会存为临时文件，在缓存里，那么这个函数就是清除这里产生的缓存。

2. urllib.quote(url)和urllib.quote_plus(url)
将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受。
简单的看一下效果。
```
>>>import urllib
>>> urllib.quote('http://www.baidu.com')
'http%3A//www.baidu.com'
>>> urllib.quote_plus('http://www.baidu.com')
'http%3A%2F%2Fwww.baidu.com'
```

3. urllib.unquote(url)和urllib.unquote_plus(url)
与上一个函数功能相反，将编码后的url还原。

那么到这里我们的urllib函数就讲完了，是不是功能很强大呢？别担心，还有更强大的呢~

##urllib2

####基本使用
urllib2作为urllib的升级版，基本功能和使用是和urllib一致的，也可以用urlopen来发送一个请求，如下所示：
```python
import urllib2
url = 'http://www.baidu.com'
page = urllib2.urlopen(url)
html = page.read()
print html
```
保存为urllib2_demo.py,运行，看一下结果。
![urllib2_baidu_HTML](urllib2_baidu.jpg)
可以看到跟urllib的基本写法一致，返回结果也一致。

但是这只是看起来一致而已，如果我们去翻看官方手册的话就会看到其实它们的参数有一定的不同。`urllib.urlopen(url[,data[,proxies]])`和`urlopen (url [,data [,timeout]])`虽然前两个参数都是http请求地址URL和传输的数据data，但是第三个参数由没什么用的proxies换为了超时时间timeout，即在中断连接前尝试的时间，这样的话可以设定http请求如果超过多长时间就放弃，避免长时间的等待，浪费网络资源。

####进阶操作
######urllib2.Request()
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
![urllib2_baidu_HTML2](urllib2_baidu2.jpg)
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
```
保存为urllib2_post.py，运行，看一下结果。

![urllib2_POST](urllib2_post.jpg)
确实可以发送一个带着http请求头的post请求，虽然看不出来与之前有什么区别。
那么既然可以发送post请求，那么用之前的第二种方法发送get请求当然也可以，这里就不再做演示了。

######urllib2.build_opener()
基本的urlopen()函数不支持验证、cookie或其他HTTP高级功能。要支持这些功能，必须使用build_opener()函数来创建自己的自定义Opener对象
####urllib2其他函数
1. urllib2设置代理
2. urllib2检测重定向
3. urllib2设定cookie
4. urllib2打开错误日志

####urllib与urllib2的区别
urllib与urllib2还是有一定的区别的，除了我们前面所说的urlopen的参数不一样之外，因为这些区别，使urllib和urllib2同样重要，两者配合使用，才能发挥更大威力。
- urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL。这意味着，你不可以通过urllib模块伪装你的User Agent字符串等（伪装浏览器）。
- urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。所以urllib2发送GET请求或者POST请求都需要urllib的帮助，这也是为何urllib常和urllib2一起使用的原因。
- urllib2模块比较优势的地方是urlliburllib2.urlopen可以接受Request对象作为参数，从而可以控制HTTP Request的header部。
- 但是urllib.urlretrieve函数以及urllib.quote等一系列quote和unquote功能没有被加入urllib2中，因此有时也需要urllib的辅助。

##requests
####安装
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

- 通过IDE安装吧，如pycharm！


####基本使用
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

####进阶操作
######requests发送请求
但是它和urllib又有不同之处，urllib默认的是发送get请求，但是requests需要指定发送哪种请求，看似更加复杂，但是其实让我们获得更多的选择更便利。requests支持GET/POST/PUT/DELETE/HEAD/OPTIONS等请求类型，它们的使用也非常方便。

```python
>>> r = requests.get("http://httpbin.org/get")
>>> r = requests.post("http://httpbin.org/post")
>>> r = requests.put("http://httpbin.org/put")
>>> r = requests.delete("http://httpbin.org/delete")
>>> r = requests.head("http://httpbin.org/get")
>>> r = requests.options("http://httpbin.org/get")
```

>KISS -- Keep　It　Simple  Stupid
>一切本该如此简单

那么既然可以发送GET或者POST请求，那它们的参数在哪里呢？
就在requests()的第二个和第三个参数，第二个参数params，第三个参数data，分别用来接收get和post的数据。
我们还是来试一下发送请求给本地服务器看一下结果怎么样，还是form_get.php和form_post.php.php。
```python
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
![requests_request](requests_request.jpg)
确实都能够成功的发送相应的请求。
requests除了能够更方便的发送请求之外，还将urllib里面的复杂的操作简化了很多。
上面的例子可以看出来get或者post请求时发送的数据不需要再经过打包就可以直接发送，其实像这样的简化还有不少，比如说headers。
```python
import requests
url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.12 Safari/537.36'} 
page = requests.get(url=url,headers=headers)
html = page.content
print html
```
保存为requests_headers.py,运行，看一下结果。
![requests_headers](requests_headers.jpg)
可以看出来，还是结果没什么变化，但是它的语法规则比urllib更简洁了不少。
在这里，不但可以设定请求头，也可以作为查看请求头来使用，例如`page.requests.headers`就可以查看请求头。

######requests上传文件
使用 Requests 模块，上传文件也是如此简单的，文件的类型会自动进行处理。
我们来试一下用post方法向我本地服务器上传一张照片。
服务器上的php代码如下。
```php
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
#coding=utf-8
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
![requests_file](requests_file.jpg)
上传成功，而且更加方便的是，你可以把字符串当着文件进行上传，就是自己边创建文件边上传，如下所示。
```python
#coding=utf-8
import requests
url = 'http://localhost/upload/1/upload.php'
data = {'submit':'true'}
#必需自己设定设置文件名
files = {'file': ('test.txt', b'Hello Requests.')}     
page = requests.post(url, data=data,files=files)
html = page.content
print html
```
保存为requests_file2.py,运行，看一下结果。
![requests_file2](requests_file2.jpg)
也是能够上传成功的。

######requests其他功能
- 身份验证
 - 基本身份认证(HTTP Basic Auth)
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
![requests_basicauth](requests_basicauth.jpg)
 - 摘要式身份认证(HTTP Digest Auth)
写法与上类似`requests.get(URL, auth=HTTPDigestAuth('user', 'pass'))`不在做详细阐述。

- cookies与session
 - 获得cookies。比如说我们在访问Baidu时，它就会自动的给我们设定一个cookies，现在让我们来看一下这些cookies。
```python
import requests
r = requests.get('http://www.baidu.com')
print r.cookies['BAIDUID']
print r.cookies
```
保存为requests_getcookie.py,运行，看一下结果。
![requests_getcookie](requests_getcookie.jpg)
可以看出来一连串的cookies，那么这些是服务器给我们设定的cookies，如果服务器需要我们向它发送cookies的话要怎么办呢？
 - 发送cookies。比如说很多网站都有保存密码的功能，就是在你每次访问站点是先检查你本机的cookies，cookies里面存储了你的账户名和密码，如果你的cookies存在且正确，就可以直接登录，不再需要输入账户名和密码。
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
import requests
url = 'http://localhost/cookies.php'
cookies = {'name': 'admin', 'email': 'me@wenqiangyang.com'}
page = requests.get(url, cookies=cookies)
html = page.content
print html
```
保存为requests_setcookie.py，运行，看一下结果。
![requests_setcookie](requests_setcookie.jpg)
除了cookies之外，还有session，不过这个session可不是保存在服务器端的那个session，那个session是服务器设定的保存在服务器端的我们也没有办法更改，此处的session是指我们在与某个URL通信发送http请求时，保持会话，让同一个cookies长期有效，因为有可能你需要发送不止一次的http请求，又不想每次发送请求的时候都带上cookies。同一个Session实例发出的所有请求之间保持cookies，且这些都是自动处理的，甚是方便。
这里我没有什么实例了，在网上找到了一个快盘签到脚本，感兴趣的同学可以试一下。
```
import requests
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
s = requests.Session()
s.headers.update(headers)
# s.auth = ('superuser', '123')
s.get('https://www.kuaipan.cn/account_login.htm')
_URL = 'http://www.kuaipan.cn/index.php'
s.post(_URL, params={'ac':'account', 'op':'login'},
       data={'username':'****@foxmail.com', 'userpwd':'********', 'isajax':'yes'})
r = s.get(_URL, params={'ac':'zone', 'op':'taskdetail'})
print(r.json())
s.get(_URL, params={'ac':'common', 'op':'usersign'})
```
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
 - verify。Requests可以为HTTPS请求验证SSL证书，就像web浏览器一样。要想检查某个主机的SSL证书，你可以使用 verify 参数。当使用requests.get(url)抓取HTTPS网页时，会遇到requests.exceptions.SSLError错误，可能是因为该网页SSL证书失效，这时需要将verify设置为False即可。默认为True。


######requests返回对象
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
import requests
url = 'http://www.baidu.com'
page = requests.get(url=url)
code = page.status_code
headers = page.headers
print code
print headers
```
保存为requests_info.py,运行，看一下结果。
![requests_info](requests_info.jpg)
好吧，运行结果是正常的，就是headers那里是直接输出了，没有urlopen返回对象用info()解析的那么好看，没事，我们自己来排版一下就可以。
```python
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
![requests_info2](requests_info2.jpg)
这下好看多了，结果显示也是和urlopen返回对象的info()的结果类似。



主要参考链接：

[Python核心模块——urllib模块](http://www.cnblogs.com/sysu-blackbear/p/3629420.html)

[urllib模块和urllib2模块的区别](http://www.cnblogs.com/sysu-blackbear/p/3630178.html)

[Python 第三方 http 库-Requests 学习](http://www.itwhy.org/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/python/python-%E7%AC%AC%E4%B8%89%E6%96%B9-http-%E5%BA%93-requests-%E5%AD%A6%E4%B9%A0.html)

[python requests的安装与简单运用](http://www.zhidaow.com/post/python-requests-install-and-brief-introduction)

[requests官方文档-安装](http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/install.html#install)

[requests官方文档-快速上手](http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/quickstart.html)

[requests官方文档-高级用法](http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/quickstart.html)















  
