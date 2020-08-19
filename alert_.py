# 警告框处理

# 使用switch_to_alert()方法定位到JavaScrip所生成的alert/confirm/prompt,
# 然后使用text/accept/dismiss/send_keys等方法进行操作
# 1. text: 返回alert/confirm/prompt中的文字信息
# 2. accept(): 接受现有警告框
# 3. dismiss(): 解散现有警告框
# 4. send_keys(keysToSend): 发送文本至警告框。eysToSend：将文本发送至警告框

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("httP://www.baidu.com")

# 鼠标悬停
setting = driver.find_element_by_id("s-usersetting-top")
ActionChains(driver).move_to_element(setting).perform()

# ctrl+shift+c 固定悬停后的元素进行定位
driver.find_element_by_link_text("搜索设置").click()
driver.find_element_by_link_text("保存设置").click()

# 接受警告框
driver.switch_to_alert().accept()

driver.quit()