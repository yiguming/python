#!/usr/bin/python
class MoneyFmt(object):
	def __init__(self,value = 0.0):
		self.value = float(value)
	def update(self,value = None):
		if value != None:
			self.value = float(value)
			print 'Value has been updated. the new value is :',self.value
		else:
			print 'Value has not been updated'
	#def __nonzero__(self,value):
	#	if value != 0:
	#		return True
	#	else:
	#		return False
	def __nonzero__(self):
		return int(self.value)
	def __repr__(self):
		return repr(self.value)
	def __str__(self):
		val = ''
		roundi = round(i,2)
		absi = abs(roundi)
		if (absi * 10 ) % 1 ==0:
			value = format(absi,',') + '0'
		else:
			value = format(absi,',')
		if roundi >=0:
			val = '$' +value
		else:
			val = '-' + '$' + value

		return val



def dollarize(i):
	roundi = round(i,2)
	absi = abs(roundi)
	if (absi * 10 ) % 1 ==0:
		value = format(absi,',') + '0'
	else:
		value = format(absi,',')
	#value = format(absi,',')
	if roundi >=0:
		return '$' + value
	else:
		return '-' + '$' +value




if __name__ == '__main__':
	print dollarize(-1234567.8901)
	print dollarize(1234567.8901)
	print dollarize(1234567.80) 

	