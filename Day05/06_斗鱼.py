from selenium import webdriver
import time
num = 1
# 创建浏览器对象
driver = webdriver.Chrome()


# 进入斗鱼TV直播
driver.get('https://www.douyu.com/g_wzry/')


while True: 
    rList = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li/a/div/p')
    for r in rList:
        contentList = r.text.split('\n')
        name = contentList[0]
        hot = contentList[1]
        d = {
                "主播":name,
                "热度":hot,
                }
        with open('douyu.json',"a",encoding="utf-8") as f:
            f.write(str(d) + "\n")
    if driver.page_source.find('shark-pager-next shark-pager-disable shark-pager-disable-next') == -1:
        driver.find_element_by_class_name('shark-pager-next').click()
        print("正在爬取第%d页"%num)
        num += 1
        time.sleep(1)
    else:
        print("爬取结束")
        break