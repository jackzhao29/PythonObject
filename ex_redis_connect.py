#coding:utf-8
#redis使用示例
'''
redis-py使用connection pool管理对一个redis server的所有连接，避免每次建立、释放连接所带来的开销。
默认每个Redis实例都会维护一个自己的连接池，可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个
Redis实例共享一个连接池
'''
import redis

pool = redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)
r = redis.Redis(connection_pool=pool)
'''
redis pipeline机制可以在一次请求中执行多个命令，这样可以避免多次往返时延
redis-py默认在一次pipeline中的操作是原子的，要改变这种方式，可以传入transaction=False
'''
pipe = r.pipeline(transaction=False)
pipe.set('one', 'first')
pipe.set('two','second')
pipe.set('zhangsan', '张三')
pipe.set('lisi','李四')
pipe.execute()

print r.get('one')
print r.get('two')
print r.get('zhangsan')

#第二种写法
pipe.set('jack','jacks').rpush('list', 'hello').rpush('list','world').execute()

print r.get('jack')
print r.lrange('list',0,-1)
