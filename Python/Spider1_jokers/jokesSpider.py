from urllib import  request,parse
import  re

file_log="./log.txt"
file_joke="./jokers.txt"
page=1
url="http://www.qiushibaike.com/8hr/page/"
url_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
headers={
    'User-Agent':url_agent,
}
req=request.Request(url+str(page),headers=headers)
with request.urlopen(req)as resp:
    print(resp.status,resp.reason)
    content=resp.read().decode('utf-8')
    if resp.status==200 :
        with open(file_log,'w',encoding='utf-8') as f:
            f.write(content)
    m=(	'div.*?author.*?img.*?<a.*?<h2>(.*?)</h2'
        '.*?<div.*?content.*?span>+(.*?)</span'
        '.*?<span.*?stats-vote.*?number.*?>(.*?)</i>'
        # '(.*?<span class="cmt-name.*?>(.*?)</span>)*?'
    )
    patten=re.compile(m,re.S)
    items= re.findall(patten,content)
    for item in items:
        for i in item:
        	print(i)


