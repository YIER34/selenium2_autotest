from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
driver.quit()
