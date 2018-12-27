from urllib.request import Request,urlopen
from urllib.parse import urlencode

class BaiduSpider:
    def __init__(self):
        self.baseurl = 'http://tieba.baidu.com/f?'
        self.headers = {'User-Agen':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    # 获取页面内容
    def getPage(self,url,headers):
        req = Request(url,headers=self.headers)
        res = urlopen(req)
        html = res.read().decode('utf-8')
        return html
    # 解析页面
    def parsePage(self):
        pass
    # 保存数据
    def writePage(self,filename,html):
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)
    # 主函数
    def workOn(self):
        name = input("请输入要抓取的贴吧名称:")
        start = int(input("请输入起始页:"))
        end = int(input("请输入终止页:"))
        kw = urlencode({'kw':name})
        for page in range(start,end+1):
            # 拼接第page页完整的URL地址
            pn = (page - 1) * 50
            url = self.baseurl+kw+'&pn='+str(pn)
            html = self.getPage(url,self.headers)
            filename = "第%d页.html"%page
            self.writePage(filename,html)
            print("第%d页爬取成功"%page)


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.workOn()