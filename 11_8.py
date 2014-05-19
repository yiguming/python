#!/usr/bin/python
def isLeapYear(year):
	if (year % 4 ==0 and year % 100 !=0) or (year %400 ==0):
		leapyear = 1
	else:
		leapyear = 0
	return leapyear

lst_year = [1992,1996,2000,1967,1900,2400]
print filter(isLeapYear,lst_year)
print [eachyear for eachyear in lst_year  if isLeapYear(eachyear)]

