#coding=utf-8
import re

data = r"multiName = raw_input(\"Please Input Your nodady@xxx.xxx.com http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html Attachment Name:\n\")message = MIMEMultipart()attr = MIMEText(open(multiName,\"rb\").read(),\"base64\",\"utf-8\")attr[\"Content-Type\"] = 'application/octet-stream'attr[\"Content-Disposition\"] = 'attachment; filename=\"%s\"'%(multiName)message.attach(attr)content = me@wenqiangyang.comMIMEText(messageContent,\"plain\",\"utf-8\")smtp.163.commessage.attach(content)"
# m = re.search('multi.{2}[maeiou][aeiou]',data)
# m = re.search('\w*.in[aeioupt]{1,9}',data)
# m = re.search("\w*@(\w*\.)?\w*\.com",data)

# m = re.search(r"\b(\w*)\_(\w*)",data)
# if m is not None:
# 	print m.group(1)
# 	print m.group(2)
# 	print m.groups() 

# m = re.findall(r"\w{3}.\w{3}",data)
# m = re.findall(r"\w{3}[^a-zA-Z]\w{3}",data)
# if m is not None:
# 	print m

# print re.sub('[ao]',"X","aeiouaeiou")
# print re.subn('[ao]',"Y","aeiouaeiou")

# print re.split("[o]","aeiouaeiou")


# m = re.search(r"")