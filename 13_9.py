#!/usr/bin/python
class Queue(object):
	"""docstring for Queue first-in-firt-out"""
	def __init__(self, queuelist):
		self.queuelist = queuelist
	def enqueue(self,buttonitem):
		self.queuelist.append(buttonitem)
		print 'The new button item is ',buttonitem,'\n'
		print 'The update queuelist is ',self.queuelist,'\n'
	def dequeue(self):
		headItem =  self.queuelist[0]
		print 'The headItem ',headItem,'has been deleted'
		self.queuelist = self.queuelist[1:]
		print 'The update queuelist is ',self.queuelist,'\n'

a_queuelist =Queue([1,2,3,4,5,6,7,8])
a_queuelist.enqueue(9)
a_queuelist.enqueue(0)
a_queuelist.dequeue()



