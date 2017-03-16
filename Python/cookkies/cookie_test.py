#cookie用来保存打开一个网站后的一些临时数据，一般用来存用户登入信息。
#访问一些需要登入的网页必须携带cookie信息才能正常访问，浏览器自动帮我们保存了cookie信息，
#而用python的话就得自己存储并携带cookie来访问网站了。
#python3.0之后去掉了cookielib模块，原来的cookiejar类被包在了http模块下 包括FileCookieJar类

from http import cookiejar
from urllib import request,parse

username=""
passwd=""
loginurl="http://"
afterloginurl="http://"
afterloginurl2="http://"

filename="./cookie.txt"
req=request.Request(loginurl)
cookie=cookiejar.MozillaCookieJar(filename)#使用MozillaCookieJar创建一个cookie
handler=request.HTTPCookieProcessor(cookie)#创建一个cookie处理器
opener=request.build_opener(handler)#创建一个访问器
data={
	"log":username,
	"pwd":passwd,
	"wp-submit":"登录",
	"redirect_to":afterloginurl
}
datacode=parse.urlencode(data);#构建post请求数据包

req=opener.open(req,data=datacode.encode("utf-8"))#发送请求

#登入成功后保存cookie到本地,为了以后可以用cookie直接访问
#注意save的时候一定要填上 这两个参数 ignore_discard=True,ignore_expires=True 
cookie.save(ignore_discard=True,ignore_expires=True);


#然后打开一个登入后的后台管理业，并把html输出到文件，之后打开html文件就能看到登入成功后的页面了
rep=opener.open(afterloginurl2)
log=open("./log.html","w")

print(rep.status,rep.reason)
log.write(rep.read().decode('utf-8'))
log.close();