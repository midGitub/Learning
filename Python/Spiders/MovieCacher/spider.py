from urllib import  request
import  config
import  urllib

class spider:

    def __init__(self):
        self.urlSet={}

    def getPageCode(self,url,agent):
        headers={"User-Agent":agent}
        req=request.Request(url,headers=headers)
        try:
            resp=request.urlopen(req)
            content=resp.read().decode('utf-8')
            if content:
                with open("./spider_log.txt","w",encoding='utf-8')as f:
                    f.write(content)
            return content

        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print('Error:',e.status,e.reason)
            return  None


if __name__=='__main__':
    spid=spider()
    print(spid.getPageCode(config.url,config))

