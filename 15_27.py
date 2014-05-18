#!/usr/bin/env python
import re

patt = r'\w+ (\w+) (\d?\d) \d\d:\d\d:\d\d\s+(\d\d\d\d)'
#print all the time 
with open("redata1.txt") as fobj1:
    for item in fobj1:
        m = re.match(patt,item)
        if m is not None:print m.group(1),m.group(2),',',m.group(3)
print 'Done'
