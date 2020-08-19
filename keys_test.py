# 键盘事件

from selenium import webdriver
# 引入keys模块
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_id("kw").send_keys("seleniumm")
# 1. 删除多输入的一个字符m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 2. 输入空格键
driver.find_element_by_id("kw").send_keys(Keys.SPACE)

# 3. ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# 4. ctrl+c 复制输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'c')
# 5. ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# 6. ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

# 7. 通过回车键代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)

# 8. 制表键
driver.find_element_by_id("kw").send_keys(Keys.TAB)

# 9. 回退键
driver.find_element_by_id("kw").send_keys(Keys.ESCAPE)

# 10. 键盘F1-F12
driver.find_element_by_id("kw").send_keys(Keys.F1)

