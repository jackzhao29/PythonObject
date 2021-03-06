#coding:utf-8
'''
OOP创建线程
'''

import threading
import time
import os

def doChore():
    time.sleep(0.5)

class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].acquire()
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1
                print(self.tid,':now left:',monitor['tick'])
                doChore()
            else:
                print("Thread_id",self.tid,'No more tickets')
                os._exit(0)
            monitor['lock'].release()
            doChore()

monitor = {'tick':100, 'lock':threading.Lock()}

for k in range(5):
    newThread = BoothThread(k,monitor)
    newThread.start()
