# 鼠标事件，封装在ActionChains,常用方法如下：
# perform()  执行所有ActionChains中存储的行为,可理解为对整个操作的提交
# context_click()  右击
# double_click()  双击
# drag_and_drop(source,target)  拖动,source:拖动的源元素，target：释放的目标元素
# move_to_element()  鼠标悬停


# 1. 右击操作
from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('http://yunpan.360.cn')

right_click = driver.find_element_by_id("xxxx")
# 调用类--指定右击元素--提交
ActionChains(driver).context_click(right_click).perform()

# 2. 鼠标悬停
above = driver.find_element_by_id("xxxx")
ActionChains(driver).move_to_element(above).perform()

# 3. 鼠标双击操作
double_click = driver.find_element_by_id("xxxx")
ActionChains(driver).double_click(double_click).perform()

# 4.鼠标拖放操作 
source = driver.find_element_by_id("xxxx")
target = driver.find_element_by_id("xxxx")
ActionChains(driver).drag_and_drop(source,target).perform()


