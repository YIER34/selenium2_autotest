# 单线程
from time import ctime,sleep

def music(func,loop):
    for i in range(loop):
        print("I was listening to %s! %s" %(func,ctime()))
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)
if __name__ == "__main__":
    music("麻雀",3)
    movie("阿凡达",2)
    print('all end:',ctime())