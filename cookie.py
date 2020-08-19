# 操作cookie

# webdriver 操作cookie 的方法：
# get_cookies()  获得所有cookie信息
# get_cookie(name)  返回字典的key为"name"的cookie信息
# add-cookie(cookie_dict)  添加cookie，cookie_dict包括name和value
# delete_cookie(name,optionsString)  删除cookie信息，"optionsString"指cookie选项，当前支持路径/域
# delete_all_cookies()  删除所有的cookie信息

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

# 获得cookie信息
cookies = driver.get_cookies()
print(cookies)


# 向cookie的name和value中添加会话信息
driver.add_cookie({'name':'key-aaaaa','value':'value-bbbbb'})
# 遍历cookies中的name和value信息并打印
for cookie in driver.get_cookies():
    print("%s --> %s" % (cookie['name'],cookie['value']))

# 删除某一个cookie
driver.delete_cookie('key-aaaaa')
cookies = driver.get_cookies()
print(cookies)
driver.quit()