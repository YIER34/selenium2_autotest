# 1. 多线程
# thread模块不支持守护进程，主线程退出时，所有的子线程都被强制退出
# threading模块支持守护进程
from time import ctime,sleep
import threading
'''
def music(func,loop):
    for i in range(loop):
        print("I was listening to %s! %s" %(func,ctime()))
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)

# 创建线程数组，用于装载线程
threads = []
# 创建线程t1，并添加到线程数组
t1 = threading.Thread(target=music,args=('麻雀',3))
threads.append(t1)
# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=movie,args=('阿凡达',2))
threads.append(t2)

if __name__ == "__main__":
    # 启动线程
    for t in threads:
        t.start()
    # 守护进程（等待线程终止）
    for t in threads:
        t.join()
    print('all end:',ctime())
'''

# ||
# \/
# 2. 优化线程的创建

# 创建超级播放器
def super_player(file_,time):
    for i in range(2):
        print('Start playing: %s! %s' %(file_,ctime()))
        sleep(time)

# 播放的文件与播放时长
lists = {
    '想去海边.mp3':3,
    '梦醒时分.mp3':4,
    '阿凡达.mp4':5
}
threads = []
files = range(len(lists))


# 创建线程
for file_,time in lists.items():
    t = threading.Thread(target=super_player,args=(file_,time))
    threads.append(t)

if __name__ == "__main__":
    # 启动线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end: %s' % ctime())
    