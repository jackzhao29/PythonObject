#coding:utf-8

import pickle

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

sumer = Bird()
fn = 'a.pkl'
with open(fn, 'w') as f:
    picklestring = pickle.dump(sumer, f)


print ('读取a.pkl文件并转成对象...')
with open(fn , 'r') as f:
    summer = pickle.load(f)

print (summer.have_feather,summer.way_of_reproduction)
