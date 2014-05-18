#!/usr/bin/env python
import re
#patt_time = r'(\d{2}:\d{2}:\d{2})'
#patt_doms = r'(com|edu|net|org|gov)'
patt_email = '(\w+@\w+.\w+)'
#EMailAddrPattern = re.compile(r'::([a-z]+)@([a-z]+\.[a-z]+)::')
doms = []
with open('redata1.txt','r') as fobj:
    for item in fobj:
        match = re.sub(patt_email,'439309415@qq.com',item)
        print match 
print 'Done'