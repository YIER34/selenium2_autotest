# 自动化测试模型
# 1. 线性测试：脚本可以独立执行，不互相调用和依赖（开发和维护成本高，有重复性的代码，修改花费大）
# 2. 模块化驱动测试：把重复的操作独立成公共模块，可以被其他模块调用（测试数据不同时不能重复使用，如切换登录用户名）
# 3. 数据驱动测试：数据的参数化，实现数据和脚本的分离，数据改变引起结果改变。通过工具内置的Datapool管理
# 4. 关键字驱动测试：关键字改变引起结果改变。通过QTP、Robot Framework(RIDE)工具提供的图形化界面，以“填表格”的模式代替脚本的编写（how/who/what)

# 模块化驱动示例
from selenium import webdriver
from time import ctime,sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://test.igxpt.com/index")

# 封装登录
def login():
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

# 封装退出
def logout():
    driver.find_element_by_link_text("安全退出").click()
    driver.quit()
# 调用
login()

# 其他操作

logout()
