import time
print(time.ctime())

# or
from time import ctime
print(ctime())


# 导入time模块的所有方法
from time import * 
print(ctime())
print("休眠两秒")
sleep(2)
print(ctime())