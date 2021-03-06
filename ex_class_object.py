#coding:utf-8

## Animal is-a object look at the extra credit 
#重载_init_方法需要在init前后各有两根下划线(__init__)
class Animal(object):
	pass

class Dog(Animal):
	def __init__(self,name):
		self.name = name

class Cat(Animal):
	def __init__(self,name):
		self.name = name

class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet=None

class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

rover = Dog("Rover")
print rover

satan = Cat("Satan")
print satan

mary = Person("Mary")
mary.pet = satan
print mary.pet

frank = Employee("Frank", 120000)
frank.pet = rover

flipper =Fish()

crouse = Salmon()

harry = Halibut()