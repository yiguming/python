#!/usr/bin/python
class MyClass(object):
	def myNoActionMethod(self):
		pass

mc = MyClass()
mc.myNoActionMethod()

#myNoActionMethod()
#MyClass.myNoActionMethod()

class MyClass1(object):
	'MyClass1 class definition'
	myVersion = '1.1'
	def showMyVersion(self):
		print MyClass.myVersion

print dir(MyClass1)


print MyClass1.__name__
print MyClass1.__doc__
print MyClass1.__bases__
print MyClass1.__dict__
print MyClass1.__module__
print MyClass1.__class__


stype = type('What is your quest?')
print stype
stype.__name__ # a string 'string'
type(3.1415926)
print type(3.1425926).__name__

 
