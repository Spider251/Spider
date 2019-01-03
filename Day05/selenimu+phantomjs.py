# 导入selenium中的webdriver
from selenium import webdriver
import time

# 创建phantomjs 浏览器对象
driver = webdriver.Chrome()

# 发请求
driver.get('http://www.baidu.com')

# 获取html源码
print(driver.page_source.find('su'))

# 获取网页截屏
driver.save_screenshot('百度.png')

time.sleep(10)

# 关闭浏览器
driver.close()