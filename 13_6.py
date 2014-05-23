#!/usr/bin/python
class  Line(object):
	def __init__(self,x1=0,y1=0,x2 = 0,y2=0):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
	
	def position(self):
		self.point1 = (self.x1,self.y1)
		self.point2 = (self.x2,self.y2)
		return (self.point1,self.point2)

	def length(self):
		self.length = ((self.x1 - self.x2) **2 + (self.y1 - self.y2) **2)**0.5
		return self.length

	def slope(self):
		if self.x1 == self.x2 :
			self.slope ='None'
		else:
			self.slope = (self.y2 - self.y1) / (self.x2 *1.0 - self.x1)
		return self.slope



line1 = Line(0,0,3,4)
print 'Line position is ',line1.position()
print 'Line length is ',line1.length()
print 'Line slope is',line1.slope()
