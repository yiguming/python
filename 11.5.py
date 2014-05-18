#!/usr/bin/python
def total(purePice,puretax):
	purePrice = float(raw_input('Please input the price:...'))
	puretax = float(raw_input('Please input the tax...such as 0.11...'))
	print "You should pay:"
	print 'Subtotal: %10.2f' % purePrice
	print 'Sales Tax: %10.2f' % round(purePrice * puretax,2)
	print 'TOTAL: %10.2f' % (purePrice + round(purePrice * 0.11,2))	


def total2(purePice,puretax=0.12):
	purePrice = float(raw_input('Please input the price:...'))
	#puretax = float(raw_input('Please input the tax...such as 0.11...'))
	#if i open the line 13 ,will show a error when no tax input 
	print "You should pay:"
	print 'Subtotal: %10.2f' % purePrice
	print 'Sales Tax: %10.2f' % round(purePrice * puretax,2)
	print 'TOTAL: %10.2f' % (purePrice + round(purePrice * 0.11,2))	


if __name__ == '__main__':
	total(1000,0.11)
	total2(1000)