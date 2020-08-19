# 处理html5的视频播放
# JavaScript的内置对象arguments,为数组
# currentSrc返回当前URL
# load()加载，play()播放，pause()暂停
from selenium import webdriver
from time import ctime,sleep
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://videojs.com")

video = driver.find_element_by_xpath('body/Setion[1]/div/video')
# 返回播放文件地址

url = driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

# 播放视频
print("start")
driver.execute_script("return arguments[0].play();",video)
# 播放10s
sleep(10)

# 暂停视频
print("stop")
driver.execute_script("arguments[0].pause();",video)

driver.quit()