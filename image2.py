'''
爬取手机头像图片下载到image文件夹中
@Author 小酒窝
@Data 2019-1-28
'''
#
# //div[@id="picBody"]//p/a/img/@src 单张图片的url
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from lxml import etree
import time


class Spider:
    def __init__(self):
        self.ua = UserAgent()
        self.base_url = 'https://www.27270.com/qita/mengtu/list_27_{}.html'
        self.path = 'D:\\python学习1\\Spider\\image\\image2\\'
        self.num = 1
        self.page = 1
        self.driver = webdriver.Chrome()

    def get_html(self, url):
        res = requests.get(url, headers={'User-Agent': self.ua.random})
        res.encoding = 'utf-8'
        html = res.text
        parseHtml = etree.HTML(html)
        img_url_list = parseHtml.xpath('//div[@id="picBody"]//p/a/img/@src')
        self.write(img_url_list)

    def write(self, img_url_list):
        for img_url in img_url_list:
            res = requests.get(img_url, headers={'User-Agent': self.ua.random})
            res.encoding = 'utf-8'
            # 倒数15是保存的文件名
            filename = img_url[-15:]
            path = self.path + filename
            with open(path, 'wb') as f:
                f.write(res.content)
                print("爬取第%d张图片成功" % self.num)
            self.num += 1

    def next_html(self, i):
        self.driver.get(self.base_url.format(str(i)))
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        rList = self.driver.find_elements_by_xpath('//ul[@class="pic_list"]/li/a')
        for r in rList:
            url = r.get_attribute('href')
            self.get_html(url)

    def see(self):
        print("---------------------------")
        print('正在爬取第%d页' % self.page)
        print("---------------------------")
        self.page += 1

    def main(self):
        for i in range(1, 56):
            self.see()
            self.next_html(i)


if __name__ == '__main__':
    spider = Spider()
    spider.main()
