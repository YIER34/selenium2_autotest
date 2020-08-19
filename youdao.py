# WebElement 接口常用方法
# 1. submit()用于提交表单，例如模拟搜索框输入数据后的回车操作
# 2. 返回元素尺寸 size
# 3. 获取元素的文本 text
# 4. 获取属性值 get_attribute(name)
# 5. 设置该元素是否用户可见 is_displayed()

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')
sleep(5)

search_input = driver.find_element_by_id('translateContent')
down_link = driver.find_element_by_link_text('有道智云')
size = search_input.size
print(size)

text = down_link.text
print(text)

attribite = search_input.get_attribute('type') # 可以是id，name，type等属性
print(attribite)

result = search_input.is_displayed()
print(result)
search_input.send_keys('hello')
search_input.submit()
sleep(2)
driver.quit()

