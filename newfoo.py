#!/usr/bin/python
def newfoo(arg1,arg2,*nkw,**kw):
	'display regular args and all variable args'
	print 'arg1 is:',arg1
	print 'arg2 is:',arg2
	for eachNKW in nkw:
		print 'addition non-keyword arg:',eachNKW
	for eachNKW in kw.keys():
		print "addition keyword arg '%s': %s" %(eachNKW,kw[eachNKW])

aTuple = (6,7,8)
aDict ={'z':9}

if __name__ == '__main__':
	newfoo('wolf',3,'projects',freud=90,gamble=96)
	#more methods to pass the argvs to the fuction
	newfoo(10,20,30,40,foo=50,bar=60)
	newfoo(2,4,*(6,8),**{'foo':10,'bar':12})
	newfoo(1,2,3,x=4,y=5,*aTuple,**aDict)