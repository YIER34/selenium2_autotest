# 创建自己的线程类

import threading
from time import ctime,sleep

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    
    def run(self):
        self.func(*self.args)

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
    t = MyThread(super_player,(file_,time),super_player.__name__)
    threads.append(t)

if __name__ == "__main__":
    # 启动线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end: %s' % ctime())