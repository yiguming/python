#!/usr/bin/env python
import re
patt='(.+)::.+::\d+'
#patt = "w+ w+ \d?\d \d\d:\d\d:\d\d"
num = []
#print a time list
with open("redata.txt") as fobj:
    for item in fobj:
        print item
        m =re.match(patt,item)
        num +=re.findall(patt,item)
print num


#print all the time 
with open("redata.txt") as fobj1:
    for item in fobj1:
        m = re.match(patt,item)
        if m is not None:print m.group(1)
print 'Done'
