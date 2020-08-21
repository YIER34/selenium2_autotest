# 公共模块
from selenium.webdriver.common.action_chains import ActionChains
'''
class Login():
    
    def user_login(self,driver):
        driver.find_element_by_link_text("登录").click()
        username = driver.find_element_by_id('username')
        username.clear()
        username.send_keys("13300000002")

        password = driver.find_element_by_id('password')
        password.clear()
        password.send_keys("qwe123456789")

        source = driver.find_element_by_xpath('//*[@id="simple-slider"]/div[2]')
        # 滑动滑块
        action = ActionChains(driver)
        # 按住鼠标左键
        action.click_and_hold(source).perform()
        # 清除存储的行为
        action.reset_actions()
        # 移动鼠标的位置
        action.move_by_offset(288,0).perform()
        
        driver.find_element_by_xpath('//*[@id="btn"]').click()


    def user_logout(self,driver):
        driver.find_element_by_link_text("安全退出").click()
        driver.quit()
'''
# 修改接口做参数化
class Login():
    
    def user_login(self,driver,name,psw):
        driver.find_element_by_link_text("登录").click()
        username = driver.find_element_by_id('username')
        username.clear()
        username.send_keys(name)

        password = driver.find_element_by_id('password')
        password.clear()
        password.send_keys(psw)

        source = driver.find_element_by_xpath('//*[@id="simple-slider"]/div[2]')
        # 滑动滑块
        action = ActionChains(driver)
        # 按住鼠标左键
        action.click_and_hold(source).perform()
        # 清除存储的行为
        action.reset_actions()
        # 移动鼠标的位置
        action.move_by_offset(288,0).perform()
        
        driver.find_element_by_xpath('//*[@id="btn"]').click()


    def user_logout(self,driver):
        driver.find_element_by_link_text("安全退出").click()
        driver.quit()