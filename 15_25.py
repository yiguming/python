#!/usr/bin/env python
import re
#patt_time = r'(\d{2}:\d{2}:\d{2})'
patt_doms = r'(com|edu|net|org|gov)'
EMailAddrPattern = re.compile(r'::([a-z]+)@([a-z]+\.[a-z]+)::')
doms = []
with open('redata1.txt','r') as fobj:
    for item in fobj:
        m = re.search(patt_doms,item)
        doms  += re.findall(patt_doms,item)
print doms
print 'Done1'
with open('redata1.txt','r') as fobj:
    for item in fobj:
        m = re.search(patt_doms,item)
        if m is not None:print m.group(1)
print 'Done2'




Email = []
with open('redata1.txt','r') as fobj:
    for item in fobj:
        m = re.search(EMailAddrPattern,item)
        Email  += re.findall(EMailAddrPattern,item)
print Email
print 'Done3'
with open('redata1.txt','r') as fobj:
    for item in fobj:
        m = re.search(EMailAddrPattern,item)
        if m is not None:print m.group(1),m.group(2)
print 'Done4'



