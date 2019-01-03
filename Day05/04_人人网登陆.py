from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.set_headless()
opt.add_argument('windows-size=1920*3000')

# 创建浏览器对象
driver = webdriver.Chrome(options=opt)
# 发请求,获取响应
driver.get('https://www.renren.com/')
# 窗口最大化
driver.maximize_window()
# 找用户名,发送
uname = driver.find_element_by_name('email')
uname.send_keys('309435365@qq.com')
# 找密码,发送
pwd = driver.find_element_by_name('password')
pwd.send_keys('zhanshen001')
# 找验证码,屏幕截图,从终端输入验证码, 发送验证码
driver.save_screenshot('验证码.png')

yzm = input('请输入验证码')

driver.find_element_by_name('codeTip').send_keys(yzm)

# 点击登录按钮
driver.find_element_by_class_name('login').click()

# 屏幕截图
driver.save_screenshot('成功.png')

# 关闭浏览器
driver.close()