#!/usr/bin/env python
import re
patt_time = r'(\d{2}:\d{2}:\d{2})'
time = []
with open('redata.txt','r') as fobj:
    for item in fobj:
        m = re.search(patt_time,item)
        time  += re.findall(patt_time,item)
print time 
print 'Done1'
with open('redata.txt','r') as fobj:
    for item in fobj:
        m = re.search(patt_time,item)
        if m is not None:print m.group(1)
print 'Done2'