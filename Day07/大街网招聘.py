from selenium import webdriver
import time
num = 1
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

# 创建浏览器对象
driver = webdriver.Chrome()
driver.get('https://so.dajie.com/job/search')
driver.find_element_by_class_name('register_close').click()
key = input("搜索内容:")
# 输入框输入内容
driver.find_element_by_id('jobInput').send_keys(key)

# 点击搜索
driver.find_element_by_id('soJob').click()
time.sleep(2)

while True:
    # 执行脚本, 滚动进度条拉倒最底部
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    rList = driver.find_elements_by_xpath('//div[@id="container_jobList"]//li')
    #print(rList)
    for r in rList:
        content = r.text.split('\n')
        work = content[0]
        money = content[1].split('|')[0]
        address = content[1].split('|')[1]
        education = content[1].split('|')[3]
        company = content[2]    
        people = content[3].split('|')[1]
        print(work,money,address,company,people)
    if driver.page_source.find('next') != -1:
        driver.find_element_by_class_name('next').click()
        print("正在爬取第%d页"%num)
        num += 1
        time.sleep(1)
    else:
        print("爬取结束")
        break