#!/usr/bin/python
def CustomerChoice():
	while True:
		print 'Please select:'
		print "To create a new 'clean' file,please input  'N'."
		print "To overwrite a existing file,please input 'O'."
		Input = raw_input('Your choice is :... ')
		if Input =='N':
			return True
			break
		elif Input =='O':
			return False
			break
		else:
			print 'Error input ,try again.'


def LineProcess(eachLine):
	return (eachLine.lstrip()).rstrip()
	


textFile = open('spacetest.txt','r')
newLines = map(LineProcess,textFile)
print newLines
textFile.close()

customerInput = CustomerChoice()
if customerInput: 
	newFile = open('newfile.txt','w')
	for eachLine in newLines:
		newFile.write(eachLine +'\n')
	newFile.close()

else:
	overwriteFile = open('spacetest','w')
	for eachLine in newLines:
		overwriteFile.write(eachLine + '\n')
	overwriteFile.close()

