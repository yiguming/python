#!/usr/bin/ptyon
def tupleVarArgs(arg1,arg2 ='defaultB',*theRest):
	'dispaly regular args and non-keyword variable args'
	print 'formal arg 1:',arg1
	print 'formal arg 2:',arg2
	for eachXtrArg in theRest:
		print 'another arg:',eachXtrArg

if __name__ == '__main__':
	tupleVarArgs('abc')
	tupleVarArgs(23,4.56)
	tupleVarArgs('abc',123,'xyz',456.789,'guming')