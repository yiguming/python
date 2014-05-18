#!/usr/bin/python 
print max(4,8)
print min(4,  8  )
print max([1,2,3,4,5])
print max('12','0123','111')
def max2(x,y):
	if x >y:
		return x
	else:
		return y
def min2(x,y):
	if x >y:
		return y
	else:
		return x
def my_max(*data):
	ret = data[0]
	for i in data:
		print i +"debbuing" 
		ret = max2(ret,int(i))
		print ret
	return ret
def my_max2(lst):
	ret = lst[0]
	for i in range(len(lst)):
		ret = max2(ret,lst[i])
	return ret


def my_min(*data):
	ret = data[0]
	for i in data:
		ret = min2(ret,i)
	return ret
def my_min2(lst):
	ret = lst[0]
	for i in range(len(lst)):
		ret = min2(ret,lst[i])
	return ret
if __name__ =='__main__':
	print my_max('12','0199','22') + "error"
	print my_max2([12,123,199])
	print my_min('1222','12','5','7') +"error"
	print my_min2([100,2,33,44,1,66,43])

