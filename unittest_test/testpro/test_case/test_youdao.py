from selenium import webdriver
import unittest
import time 

class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("webdriver")
        driver.find_element_by_xpath('//*[@id="form"]/button').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,"【webdriver】什么意思_英语webdriver的翻译_音标_读音_用法_例句_在线翻译_有道词典")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()