from selenium import webdriver
from time import ctime,sleep
from selenium.webdriver.common.action_chains import ActionChains
from pubilc import Login
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://test.igxpt.com/index")
'''
# 调用登录模块
Login().user_login(driver)

# 调用退出模块
Login().user_logout(driver)
'''
# 调用登录模块--参数化
class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://test.igxpt.com/index")

    # 供应商登录
    def test_seller_login(self):
        username = "13300000002"
        password = "qwe123456789"
        Login().user_login(self.driver,username,password)
        self.driver.quit()

    # 采购商登录
    def test_buyer_login(self):
        username = "13700000066"
        password = "qwe123456789"
        Login().user_login(self.driver,username,password)
        self.driver.quit()
LoginTest().test_buyer_login()
LoginTest().test_seller_login()
        