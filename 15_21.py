#!/usr/bin/env python
import re
patt_month = r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
mon = []
with open('redata.txt','r') as fobj:
    for item in fobj:
        m = re.search(patt_month,item)
        mon = mon + re.findall(patt_month,item)
print mon
print 'Done1'
with open('redata.txt','r') as fobj:
    for item in fobj:
        m = re.search(patt_month,item)
        if m is not None:print m.group(1)
print 'Done2'