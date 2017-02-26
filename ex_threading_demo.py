#coding:utf-8
'''
多线程售票及同步示例
'''

import threading
import time
import os

def doChore():
    time.sleep(0.5)

def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()
        if i != 0:
            i = i - 1
            print(tid,':now left:',i)
            doChore()
        else:
            print("Thread_id",tid," No more tickets")
            os._exit(0)
        lock.release()
        doChore()

i = 100
lock = threading.Lock()

for k in range(10):
    newThread = threading.Thread(target=booth,args=(k,))
    newThread.start()
