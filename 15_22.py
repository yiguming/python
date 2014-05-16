#!/usr/bin/env python
import re
patt_year = r'(\d{4})'
year = []
with open('redata.txt','r') as fobj:
    for item in fobj:
        m = re.search(patt_year,item)
        year += re.findall(patt_year,item)
print year
print 'Done1'
with open('redata.txt','r') as fobj:
    for item in fobj:
        m = re.search(patt_year,item)
        if m is not None:print m.group(1)
print 'Done2'