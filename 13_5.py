#!/usr/bin/python
class Point(object):
	"""stand for x and y of  a point """
	def __init__(self, x=0,y=0):
		self.xzuobiao =x
		self.yzuobiao =y 

j = Point()

print j.xzuobiao
print j.yzuobiao

j = Point(x=9)
print j.xzuobiao
print j.yzuobiao

j = Point(1)
print j.xzuobiao
print j.yzuobiao

j = Point(1,2)
print j.xzuobiao
print j.yzuobiao