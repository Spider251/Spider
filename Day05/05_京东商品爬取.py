from selenium import webdriver
import time
num = 1
# 创建浏览器对象
driver = webdriver.Chrome()

# 访问京东首页
driver.get('https://www.jd.com')

# 找到搜索框 输入 并回车
key = input('请输入搜索的内容:')
text = driver.find_element_by_class_name('text')
text.send_keys(key)

driver.find_element_by_class_name("button").click()
time.sleep(2)
while True:
    # 执行脚本, 滚动进度条拉倒最底部
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # 提取数据
    rList = driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
    # rList : ['商品1节点对象','商品2节点对象'...]
    for r in rList:
        contentList = r.text.split('\n')
        price = contentList[0]
        name = contentList[1]
        commit = contentList[2]
        market = contentList[3]
        d = {
                "价格":price,
                "名称":name,
                "评论":commit,
                "商家":market,
                }
        with open("jd.json","a",encoding="utf-8") as f:
            f.write(str(d) + "\n")
    # 点击下一页
    if driver.page_source.find('pn-next disabled') == -1:
        driver.find_element_by_class_name('pn-next').click()
        print("正在爬取第%d页"%num)
        num += 1
        time.sleep(1)
    else:
        print("爬取结束")
        break