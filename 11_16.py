#!/usr/bin/python 
#add mulilt
from operator import add,sub,mul,div
from random import randint,choice

ops = {'+':add,'-':sub,'*':mul,'/':div}
MAXTRIES =2 

def doprob():
	op = choice('+-*/')
	nums = [randint(1,10) for i in range(2)]
	nums.sort(reverse=True)
	if op != '/':
		ans = ops[op](*nums)
		pr = '%d %s %d =' % (nums[0],op,nums[1])
	else:
		ans = div(nums[0],nums[1])
		if div (nums[0] * 10,nums[1]) ==ans * 10:
			pr = '%d %s %d = ' %(nums[0],op,nums[1])
		else:
			ans = mul(num[0],nums[1])
			pr = '%d %s %d =' (nums[0], ' *',nums[1])
	opps =0
	while True:
		try:
			if int(raw_input(pr)) == ans:
				print 'correct'
				break
			if opps == MAXTRIES:
				print 'answer\n %s%d'%(pr,ans)
			else:
				print 'incorrect ...try again'
				opps +=1
		except (KeyboardInterrupt, \
			EOFError,ValueError):
			print 'invalid input...try again'

def main():
	while  True:
		doprob()
		try :
			opt = raw_input('Again?[y]').lower()
			if opt and opt[0] =='n':
				break
		except (KeyboardInterrupt,EOFError):
			break

if __name__ == '__main__':
	main()
