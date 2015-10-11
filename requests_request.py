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