#!/usr/bin/env python
import re
patt_email = '(\w+@\w+.\w+)'
ema = []
#print all email in a list
with open("redata.txt",'r') as fobj:
    for item in fobj:
        m =re.search(patt_email,item)
        ema +=re.findall(patt_email,item)
print ema
print 'Done'


#print all email one by one
with open("redata.txt",'r') as fobj1:
    for item in fobj1:
        m = re.search(patt_email,item)
        if m is not None:
            print m.group(1)
print 'Done'
