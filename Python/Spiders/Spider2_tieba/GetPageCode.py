from urllib import  request,parse
import  re

logfile="log.txt"
url="https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1"
agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
headers={
    "User-Agent":agent,
}
req=request.Request(url,headers=headers)
with request.urlopen(req)as resp:
    print(resp.status,resp.reason)
    content=resp.read().decode('utf-8')
    print(content)
    with open(logfile,'w',encoding='utf-8')as f:
        f.write(content)
        f.close()
