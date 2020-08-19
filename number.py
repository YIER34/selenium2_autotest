# 验证码处理
# 1. 开发直接注释掉相关代码（适用于测试环境）
# 2. 设置万能验证码
'''
from random import randint
verify = randint(1000,9999)
print("生成的随机数为:%d" %verify)
number = int(input("请输入随机数："))
print(number)

if number == verify:
    print("登录成功")
elif number == 135789:
    print("登录成功")
else:
    print("输入验证码有误")
'''
# 3. 验证码识别技术 通过Python-tesseract来识别图片验证码（识别率难以达到100%）
# 4. 记录cookie
from selenium import webdriver
from time import ctime,sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://test.igxpt.com/login")

print(cookies)
driver.find_element_by_link_text("登录").click()
username = driver.find_element_by_id('username')
username.clear()
username.send_keys("13300000000")

password = driver.find_element_by_id('password')
password.clear()
password.send_keys("qwe123456789")

source = driver.find_element_by_xpath('//*[@id="simple-slider"]/div[2]')
# target = driver.find_element_by_class_name("handle red-bar disabled")

# 滑动滑块
action = ActionChains(driver)
# 按住鼠标左键
action.click_and_hold(source).perform()
# 清除存储的行为
action.reset_actions()
# 移动鼠标的位置
action.move_by_offset(310, 0).perform()

driver.find_element_by_link_text("登录").click()

sleep(2)
# 获取用户名和密码对应的key值
cookies = driver.get_cookies()
print(cookies)

# 将用户名和密码写入浏览器cookie
driver.add_cookie({'name':'Hm_lpvt_3e059416b2038da3620af3bca51c48b8','value':'1597827848'})
driver.add_cookie({'name':'Hm_lvt_3e059416b2038da3620af3bca51c48b8','value':'1597827845'})

# 再次访问网站，将会自动登录
driver.get("https://test.igxpt.com/login")
print(cookies)
sleep(5)
driver.quit()

