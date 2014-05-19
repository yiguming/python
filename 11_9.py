#!/usr/bin/python
def mySum (x,y):
	return x + y
allNums = range(5)
total =0
for eachNum in allNums:
	total = mySum(total,eachNum)

def average(List):
	return reduce((lambda x,y :x+y),List) /float(len(List))

print "The total is %d" % total
print 'The total is:',reduce((lambda x,y :x+y),range(5))
List = range(101)
print average(List)