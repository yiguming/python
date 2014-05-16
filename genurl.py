#!/usr/bin/python 
#gen random 2000 url charcter 
from string import lowercase
from string import uppercase
from random import choice
print lowercase
print uppercase

def gen2klowercaseurl():
	url =""
	for j in range(2000):
		url = url+choice(lowercase)
	return "http://"+ url +".com" 

def gen2kuppercaseurl():
	url =""
	for j in range(2000):
		url = url+choice(uppercase)
	return "http://"+ url +".com"

print gen2klowercaseurl()
print gen2kuppercaseurl()



