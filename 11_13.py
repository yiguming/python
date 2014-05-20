#!/usr/bin/python 
import time
def timeit(func):
	start_time = time.time()
	result = func
	end_time = time.time()
	return (result,end_time - start_time)


def mySum(x,y):return x+y
allNums = range(5) #[0,1,2,3,4]
total = 0

for eachNum in allNums:
	total = mySum(total,eachNum)

print 'the total is :',total
print 'the total is:',reduce((lambda x,y :x+y) ,range(5))

#a 
def mult(x,y):return x*y
#N = int(raw_input("Please input N to test the ji of N!:"))
allnums = range(1,5)
ji = 1
for eachNum in allnums:
	ji = mult(ji,eachNum)

print 'The ji is :',ji
print 'the ji is:',reduce((lambda x,y :x*y),range(1,5))
#b


def factorial(n):
	return reduce(mult,range(n+1)[1:])





#d
def factorial_iteration(n):
	result = 1
	for eachNum in range(n+1)[1:]:
		result = result * eachNum
	return result

def factorial_lambda(n):
	return reduce((lambda x,y:x*y),range(n+1)[1:])

def factorial_recursion(n):
	if n == 0 or n == 1: 
		return 1
	else:
		return (n * factorial_recursion(n-1))

number = 6 
print timeit(factorial_iteration(number)),'\n'

print timeit(factorial_lambda(number)),'\n'

print timeit(factorial_recursion(number)),'\n'












