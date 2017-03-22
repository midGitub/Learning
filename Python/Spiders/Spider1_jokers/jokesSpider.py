from urllib import  request,parse
import  re
import  urllib

class jokespider:
    #构造函数
    def __init__(self,url,agent,pattern):
        self.pageIndex=1
        self.url=url
        self.agent=agent
        self.headers={"User-Agent":self.agent}
        self.jokers=[]#存储了每一页的笑话list
        self.pattern=pattern

    def getPageCode(self,pageIndex):
        try:
            url=self.url+str(pageIndex)
            req=request.Request(url,headers=self.headers)
            with request.urlopen(req) as resp:
                content=resp.read().decode('utf-8','ignore')
                with open("./"+__name__+"log.txt",'w',encoding='utf-8')as f:
                    f.write(content)
                    f.close()
            return content

        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print("Error",e.status,e.reason)
                return None


    def analysisPageCodeToJokers(self,pageCode,pattern):
        
        if not pageCode:
            print("页面加载失败")
            return None
        stories=[]
        pattern=pattern
        macher=re.compile(pattern,re.S)
        items=re.findall(macher,pageCode)
        for item in items:
            replaceBR=re.compile(r"<br/>")
            #item[1]=re.sub(replaceBR,"\n",item[1])
            stories.append(item)
        return stories

    def loadPage(self,pageIndex,pattern):
        pageCode=self.getPageCode(pageIndex)
        stories=self.analysisPageCodeToJokers(pageCode,pattern)
        if stories:
            self.jokers.append(stories)

    def  getOneShotStory(self,pageStories):
        for story in pageStories:
            cm=input("请输入指令，输入Q退出：")
            if cm=="Q":
                return "Q"
            print("")
            macherBR=re.compile('<br/>')
            content=re.sub(macherBR,'\n   ',story[1])
            print("作者：",story[0],'\n  ',content,"\n赞：",story[2])
            print("")

        return None

    def start(self):
        print("正在读取糗事百科，按回车查看最新段子，Q退出")
        
        while True:

            if len(self.jokers)<2:
                self.loadPage(self.pageIndex,self.pattern)
                self.pageIndex+=1

            pageStories=self.jokers[0]#取出第一页的笑话list
            del self.jokers[0]
            if self.getOneShotStory(pageStories)=="Q":
                break









