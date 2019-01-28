'''
爬取手机头像图片下载到image文件夹中
@Author 小酒窝
@Data 2019-1-28
'''
# https://www.27270.com/qita/mengtu/2016/166492_9.html 共9张
# //a/img[@alt="可爱超萌动物动漫图片集锦"]/@src
import requests
from fake_useragent import UserAgent
from lxml import etree


class Spider:
    def __init__(self):
        self.ua = UserAgent()
        self.base_url = 'https://www.27270.com/qita/mengtu/2016/166492_{}.html'
        self.path = 'D:\\python学习1\\Spider\\image\\'
        self.num = 1

    def get_html(self, url):
        res = requests.get(url, headers={'User-Agent': self.ua.random})
        res.encoding = 'UTF-8'
        html = res.text
        p = etree.HTML(html)
        img_url = p.xpath('//a/img[@alt="�ɰ����ȶ��ﶯ��ͼƬ����"]/@src')[0]
        print(img_url)
        self.write(img_url)

    def write(self, img_url):
        res = requests.get(img_url)
        res.encoding = 'utf-8'
        filename = '%d.jpg' % self.num
        path = self.path + filename
        with open(path, 'wb') as f:
            f.write(res.content)
            print("爬取第%d张图片成功" % self.num)
        self.num += 1

    def main(self):
        for i in range(1, 9):
            self.get_html(self.base_url.format(str(i)))


if __name__ == '__main__':
    spider = Spider()
    spider.main()
