#!/usr/bin/python
def countToFour1():
	for eachNum in range(5):
		print eachNum,
def countToFour2(n):
	for eachNum in range(n,5):
		print eachNum,
def countToFour3(n=1):
	for eachNum in range(n,5):
		print eachNum,
def xian():
	return "-"*10
print "start countToFour1"
countToFour1()
print xian()
print "start countToFour2"
countToFour2(2)
print xian()
countToFour2(4)
print xian()
countToFour2(5)
print xian()
print "start countToFour3"
countToFour3()
print xian()
countToFour3(2)
print xian()
countToFour3(4)
print xian()
countToFour3(5)
print xian()