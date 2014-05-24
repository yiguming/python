#!/usr/bin/python
def findPop():
	result =False
	for i in dir(list):
		if i =='pop':
			result = True
			break
	return result

class FIFOandLIFO(object):
	"""docstring for FIFOandLIFO"""
	def __init__(self,fililist):
		self.fililist =  fililist

	def shift(self):
		headItem =  self.fililist[0]
		print 'The headItem ',headItem,'has been deleted'
		self.fililist = self.fililist[1:]
		print 'The update queuelist is ',self.fililist,'\n'

	def unshift(self,headitem):
		tempList = [headitem]
		for i in self.fililist:
			tempList.append(i)
		self.fililist = tempList
		print 'Headitem',headitem,'is pushed on the head fo the list'
		print 'The update list is ',self.fililist,'\n'

	def push(self,topItem):
		self.fililist.append(topItem)
		print 'Item ',topItem,'is pushed on the top of Stack.'
		print 'The updated Stack is',self.fililist,'\n'

	def popValue(self):
		if findPop() == True:
			topItem = self.fililist.pop()
			print 'Item ',topItem ,'has been poped.'
			print 'The update Stack is ',self.fililist,'\n'
		else:
			topItem ==self.fililist[-1]  #aaa
			self.fililist = self.fililist[:-2]
			print 'Item ',topItem ,'has been poped.'
			print 'The update Stack is ',self.fililist,'\n'


a_array = FIFOandLIFO([1,2,3,4,5,6,7,8])
a_array.shift()
a_array.unshift(9)
a_array.push(10)
a_array.popValue()
