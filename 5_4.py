#/usr/bin/python
def isLeapYear(year):
	if (year % 4 ==0 and year % 100 !=0) or (year %400 ==0):
		print "The %d is a LeapYear" %year
	else:
		print "The %d is not a LeapYear" % year

if __name__ == '__main__':
	isLeapYear(1992)
	isLeapYear(1996)
	isLeapYear(2000)
	isLeapYear(1967)
	isLeapYear(1900)
	isLeapYear(2400)