#/usr/bin/python
def findPop():
	result =False
	for i in dir(list):
		if i =='pop':
			result = True
			break
	return result


class Stack(object):
	"""last-in-first-out """
	def __init__(self, stacklist):
		self.stacklist = stacklist
	def push(self,topItem):
		self.stacklist.append(topItem)
		print 'Item ',topItem,'is pushed on the top of Stack.'
		print 'The updated Stack is',self.stacklist,'\n'

	def popValue(self):
		if findPop() == True:
			topItem = self.stacklist.pop()
			print 'Item ',topItem ,'has been poped.'
			print 'The update Stack is ',self.stacklist,'\n'
		else:
			topItem ==self.stacklist[-1]  #aaa
			self.stacklist = self.stacklist[:-2]
			print 'Item ',topItem ,'has been poped.'
			print 'The update Stack is ',self.stacklist,'\n'
	def isempty(self):
		if (len(self.stacklist) == 0) :
			return True
		else:
			return False
	def peek(self):
		return self.stacklist[-1]


a_stack = Stack([0,1,2,3,4,5,6,7,8])
a_stack.push(9)
a_stack.popValue()
a_stack.popValue()
print 'Is empty Value:',a_stack.isempty()
print 'Peek Value:',a_stack.peek()


