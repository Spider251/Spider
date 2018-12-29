import requests
from lxml import etree
import urllib


class TBSpider:
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}
        self.url = 'http://tieba.baidu.com'
    
    # 获取所有的URL列表
    def getPageUrl(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        parseHtml = etree.HTML(html)
        tList = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
#        tList = [t1,t2,t3]
        print("URL获取成功")
        for t in tList:
            tLink = self.url + t
            self.getImgUrl(tLink)
#     获取单个URL
    def getImgUrl(self,tLink):
        # 获取1个帖子的响应内容
        res = requests.get(tLink,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        # 从单个帖子的html中提取图片的src
        parseHtml = etree.HTML(html)
        imgList = parseHtml.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src')
#        imgList = [i1,i2,i3]
        print("SRC获取成功")
        for img in imgList:
            self.writepage(img)
#    把图片保存到本地
    def writepage(self,img):
        # 对图片链接发起请求, 获取res.content
        res = requests.get(img,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.content
        # 写入本地文件
        filename = img[-12:]
        with open(filename,'wb') as f:
            f.write(html)
            print(filename+"下载成功")
        
#     主函数
    def main(self):
        key = input("请输入要搜索的内容:")
        begin = int(input("起始页:"))
        end = int(input("终止页:"))
        for n in range(begin,end+1):
            pn = (n-1) * 50
            params = {
                    'kw':key,
                    'pn:':pn
                    }
            params = urllib.parse.urlencode(params)
            url = self.url+'/f?'+params
            self.getPageUrl(url)

if __name__ == '__main__':
    spider = TBSpider()
    spider.main()