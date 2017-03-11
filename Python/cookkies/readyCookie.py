from http import cookiejar
from urllib import request,parse

filename="./cookie.txt"
cookie=cookiejar.MozillaCookieJar(filename)

handler=request.HTTPCookieProcessor(cookie)

#从本地cookie文件读取cookie信息，注意必须带上这两个参数 ignore_discard=True,ignore_expires=True
cookie.load(ignore_discard=True,ignore_expires=True)
opener=request.build_opener(handler)

req=request.Request("http://mot.ttthyy.com/wp-admin/edit.php")
rep=opener.open(req)

#包登入后的后台页保存到本地
log=open("./log.html","w")
print(rep.status,rep.reason)
log.write(rep.read().decode("utf-8"))
log.close()
