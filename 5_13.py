#!/usr/bin/python
def Tran(strTime):
	num = []
	num = strTime.split(":")
	return int(num[0])*60 + int(num[1])

if __name__ =="__main__":
	while True:
		strTime =raw_input("Please enter the time,like 12:12(q to quit):")
		print strTime
		if strTime.lower =='q':
			break
		print "the time is:%d minutes" %(Tran(strTime))






