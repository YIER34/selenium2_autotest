# 多表单切换
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
#driver.maximize_window()
driver.get('http://www.126.com')
sleep(5)

print("before login=====================")
# 打印当前页面title
title = driver.title
print(title)
# 打印当前页面的url
now_url = driver.current_url
print(now_url)

# 执行登录
# 1. 切换到iframe ,switch_to.frame(id/name) ,默认为id/那name，也可通过其他定位方式
xf = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(xf)
driver.find_element_by_name('email').send_keys('13700000010')
driver.find_element_by_name('password').send_keys('123456789')
driver.find_element_by_id('dologin').click()
 # 2. 跳出当前表单，switch_to.parent_content()
 # 3. 若进入了多级表单，则通过switch_to.default_content()跳回最外层页面



print("after login=========================")
# 再次打印当前页面title
title = driver.title
print(title)
# 再次打印当前页面的url
now_url = driver.current_url
print(now_url)

# 获取登录的用户名

