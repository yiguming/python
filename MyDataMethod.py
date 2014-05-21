#!/usr/bin/python
class MyDataMethod(object):
	def printFoo(self):
		print 'You invoked printFoo()'

myObj = MyDataMethod()
myObj.printFoo()


#Father Class
class AddrBookEntry(object):
	'address book entry class'
	def __init__(self,nm,ph):
		self.name  =nm
		self.phone = ph
		print 'Created instance for :',self.name
	def upgradePhone(self,newph):
		self.phone = newph
		print 'Upgraded phone # for ',self.name

#SubClass
class EmplAddrBookEntry(AddrBookEntry):
	'Employee Address Book Entry'
	def __init__(self,nm,ph,id,em):
		AddrBookEntry.__init__(self,nm,ph)
		self.empid = id
		self.email = em

	def updateEmail(self,newem):
		self.email = newem
		print 'Updated e-mail address for :',self.name



if __name__ == '__main__':
	john = AddrBookEntry('john Doe','408-555-1212')
	jane = AddrBookEntry('jane Doe','650-555-1212')
	print john
	print john.name
	print john.phone
	print jane.name
	print jane.phone
	john.upgradePhone('415-555-1212')
	print john.phone

	john = EmplAddrBookEntry('John Doe','408-555-1212',42,'john@spam.doe')
	print john
	print john.name
	print john.phone
	print john.email
	john.upgradePhone('415-555-1212')
	print john.phone
	john.updateEmail('john@doe.spam')
	print john.email





