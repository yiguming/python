#!/usr/bin/python
from random import randint
def odd(n):
	return n % 2
def oushu(n):
	return not(n % 2)
allNums=[]
for eachNum in range(9):
	allNums.append(randint(1,99))
print allNums
print filter(odd,allNums)
print filter(oushu,allNums)


#lambda type
print "lambda type"
print filter(lambda n: n % 2,allNums)
print filter(lambda n: not(n % 2),allNums)

#list type
print "list type"
print [n for n in allNums if n % 2]
print [n for n in allNums if not(n % 2)]

#import randint as ri
#using a short list
print "The short list"
from random import randint as ri 
print [n for n in [ri(1,99) for i in range(9)] if n % 2]
print [n for n in [ri(1,99) for i in range(9)] if not(n % 2)]
