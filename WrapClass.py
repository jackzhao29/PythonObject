#coding:utf-8

"""
python包装类中的授权，可以这样理解
包装类中定义了(覆盖)一个__getattr__()方法，当包装类WrapMe生成的实例通过点运算符号调用一个属性时，如果这个属性在类WrapMe生成的实例的__dict__ 和类WrapMe的__dict__和类WrapMe父类的__dict__中 都找不到时，这个__getattr__()方法被调用。

请看代码，包装类WrapMe中覆盖了__getattr__()方法，它的返回值是调用内置方法getattr()，返回被包装对象的属性。我在这个__getattr__()方法中加了2个print  语句，就很清楚这个过程了。

通过这个__getattr__()方法的返回值，是返回的是被包装对象的属性，也就是说将被包装对象的属性
授权给包装类使用。

特别要注意的是，如果被包装对象没有这个属性，那么就会报错误。

特别提示：实例属性、类属性、类中定义的方法都是属性。
"""
class WrapClass(object):
	def _init_(self,obj):
		self._data=obj

	def get(self):
		return self._data

	def _repr_(self):
		return repr(self._data)

	def _str_(self):
		return str(self._data)

	def _getattr_(self,attr):
		print attr
		print getattr(self._data,attr)
		return getattr(self._data,attr)

list=[8,9,12,67,88]
p=WrapClass(list)
print p.pop()