#!/usr/bin/python
import time
def timeit(func):
	start_time = time.time()
	result = func
	end_time = time.time()
	return (result,end_time - start_time)

def timeit2(func):
	start_time = time.clock()
	result = func
	end_time = time.clock()
	return (result,end_time - start_time)

def func(a,b):
	return a -b

if __name__ == '__main__':
	print timeit(func(2,1))
	print timeit2(func(2,1))