
# 控制浏览器窗口大小
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
driver.get("http://m.mail.10086.cn")

print("设置浏览器宽480，高800显示")
driver.set_window_size(480,800)
driver.quit()

