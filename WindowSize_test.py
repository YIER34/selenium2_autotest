'''
# 1. 控制浏览器窗口大小
from selenium import webdriver
# 关闭控制台运行的日志信息显示
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)

driver.get("http://m.mail.10086.cn")

print("设置浏览器宽480，高800显示")
driver.set_window_size(480,800)
# 最大化窗口
driver.maximize_window()
# driver.quit()
driver.quit()
'''
# 2. 控制浏览器后退、前进
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()

# 访问首页
frist_url = 'http://www.baidu.com'
print("now access %s" %(frist_url))
driver.get(frist_url)
sleep(2)
# 访问新闻页面
second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)
sleep(2)
# 退回到百度首页
print("back to  %s" %(frist_url))
driver.back()
sleep(2)
# 前进到新闻页
print("forword to %s" %(second_url))
driver.forward()
sleep(2)

driver.quit()

# 3. 模拟浏览器刷新
driver.refresh() # 刷新当前页面