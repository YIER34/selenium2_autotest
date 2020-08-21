# 设置元素等待

# 调用JavaScript

# 窗口截图 get_screenshot_as_file()

# 参数化搜索关键字
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import ctime,sleep
# driver = webdriver.Chrome(executable_path='chromedriver.exe')

'''
# 1. 显示等待
driver.get("http://www.baidu.com")
ele = WebDriverWait(driver,5,0.5).until(lambda s: s.find_element("id","kw"))
ele.send_keys("selenium")

driver.quit()

# 可理解为：

print(ctime())
for i in range(10):
    try:
        ele = driver.find_element_by_id("kw1")
        if ele.is_displayed():
            break
    except:
        pass
else:
    print("time out")
driver.close()
print(ctime())
'''
'''
# 2. 隐式等待
# 设置等待10s
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
try:
    print(ctime())
    driver.find_element_by_id("kw2").send_keys("selenium")
except Exception as msg:
    print(msg)
finally:
    print(ctime())
    driver.quit()

# 3. 定位一组元素driver.find_elements,适用于：
# 3.1 批量操作元素，例如勾选页面上的所有复选框
# 3.2 先获取一组元素，再从这组对象中过滤需要操作的元素，例如定位出页面上所有的checkbox，然后选择其中一个进行操作
'''

'''
# 4. 调用JavaScript
# 4.1 控制浏览器滑动条
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)
driver.set_window_size(600,600)

# windows.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置
# 方法的第一个参数表示水平的左间距，第二个参数表示垂直的右间距
sleep(2)
js = "window.scrollTo(100,450);"

# execute_script()方法用于执行JavaScript代码
driver.execute_script(js)
sleep(3)

# 4.2 向页面中textarea文本框输入内容，此情况无法通过send_keys输入
# 例如 html代码为：
# <textarea id="id" stytle="width:98%" cols="50" row="5" class="textarea">
# </textarea>

text = "输入的内容"
# 将text与JavaScript代码通过"+"进行拼接
js = "var sum=document.getElemantById('id');sum.value='" + text + "';"
driver.execute_script(js)
'''
'''
# 5. 窗口截图
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)
# 截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("F://selenium2_autotest/baidu_img.png")
driver.quit()
'''

# 5. 参数化搜索关键字
search_text = ['python','中文','123']
for text in search_text:

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(text)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()