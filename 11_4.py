#!/usr/bin/python
def Tran(minutes):
	num = [0,0]
	num[0] = minutes / 60
	num[1] = minutes % 60
	strTime =str(num[0])+":"+str(num[1])
	return strTime

if __name__ =="__main__":
	while True:
		minutes = int(raw_input("Please enter the minutes,like 606 (q to quit)"))
		if str(minutes) =='q':
			break
		print "The time is:%s " %(Tran(minutes))




