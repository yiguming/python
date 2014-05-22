#!/usr/bin/python
class MoneyFmt(object):
	def __init__(self,value = 0.0,flag ='-'):
		self.value = float(value)
		self.flag = flag

	def update(self,value = None):
		if value != None:
			self.value = float(value)
			print 'Value has been updated. the new value is :',self.value
		else:
			print 'Value has not been updated'
	
	def __nonzero__(self):
		return int(self.value)

	def __repr__(self):
		return repr(self.value)

	def __str__(self):
		val = ''
		roundi = round(self.value,2)
		absi = abs(roundi)
		if (absi * 10 ) % 1 ==0:
			value = format(absi,',') + '0'
		else:
			value = format(absi,',')
		if roundi >=0:
			val = '$' +value
		else:
			val = self.flag + '$' + value

		return val




	