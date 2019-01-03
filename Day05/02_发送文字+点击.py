from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.Chrome()

# 打开百度
driver.get('http://www.baidu.com')

# 找到搜索框, 发送文字
driver.find_element_by_id("kw").send_keys('美女')

# 找到 百度一下 按钮, 点击一下
driver.find_element_by_id("su").click()
# 截图
time.sleep(3)
driver.save_screenshot('美女.png')
# 关闭浏览器
driver.close()