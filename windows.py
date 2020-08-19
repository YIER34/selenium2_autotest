# 多窗口切换

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)

# 获得百度搜索窗口的句柄
search_windows = driver.current_window_handle
driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()

# 获取当前所有打开窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handles in all_handles:
    if handles == search_windows:
        driver.switch_to.window(handles)
        print("搜索窗口")
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        sleep(5)
    else:
        driver.switch_to.window(handles)
        print("注册窗口")
        driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("abcdef")
        sleep(5)
driver.quit()