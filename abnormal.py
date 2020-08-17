# 1. 异常
'''
try:
    open("abc.txt",'r')
except FileNotFoundError:
    print("程序异常")

try:
    print(aa)
except Exception:  # 2. 所有的异常类都继承Exception，Exception又继承新的基类BaseException，两者均可用来接收所有类型的异常
    print("程序异常")

try:
    print(aa)
except BaseException as msg: # 3. 返回具体异常原因
    print(msg)

# 4. try--except--else 和 try--except--finally
try:
    print(aa)
except BaseException as msg:
    print(msg)

else:
    print("没有异常才会被执行")

finally:
    print("异常与否，都会被执行") # 例如文件的关闭、锁的释放、数据库连接返还给连接池等操作
'''

# 5. 抛出异常raise(仅作示例)
from random import randint
# 生成1到9的随机整数
number = randint(1,9)
if number % 2 == 0:
    raise NameError("%d is even" %number)
else:
    raise NameError("%d is odd" %number)