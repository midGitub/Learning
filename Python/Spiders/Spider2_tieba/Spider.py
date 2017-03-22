from urllib import  request
import urllib
import re
import  config

class BDTB:

    def __init__(self,url,agent,seelz):
        self.url=url
        self.agent=agent
        self.pageIndex=1
        self.seeLz='?see_lz='+str(seelz)
        self.headers={"User-Agent":self.agent}

    def getPageCode(self,pageIndex):
        try:
            req=request.Request(self.url+self.seeLz+'&pn='+str(pageIndex),headers=self.headers)
            with request.urlopen(req)as resp:
                print(resp.status,resp.reason)
                content=resp.read().decode('utf-8')
                with open(__name__+'_log.txt','w',encoding='utf-8')as file:
                    file.write(content)
                    file.close()
            return content
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print('Error:',e.status,e.reason)
                return None

    def getTitle(self,pageCode):
        if not pageCode :
            return None

        pattern=(
            r'<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>'
        )

        title=re.search(pattern,pageCode)
        if title:
            print('GetTitle',title.group(1))
            return title.group(1)
        return None

    def getPageCount(self,pageCode):
        pattern=(r'<ul class="l_posts_num".*?<span class="red" .*?style="margin-right:3px".*?<span class="red".*?>(.*?)</span>')
        count=re.search(pattern,pageCode,re.S)
        if count:
            print('pageCount',count.group(1))
            return count.group(1)
        return None

    def getContent(self,pageCode):
        pattern=(r'<div id="post_content.*?>(.*?)</div')
        macher=re.compile(pattern,re.S)
        content=re.findall(macher,pageCode)
        print("content",len(content))
        for item in content:
            print( item.strip())
        return content



if __name__=="__main__":
    bdtb=BDTB(config.url,config.agent,1)
    pageCode=bdtb.getPageCode(1)
    bdtb.getTitle(pageCode)
    bdtb.getPageCount(pageCode)
    bdtb.getContent(pageCode)


