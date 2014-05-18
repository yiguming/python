#!/usr/bin/env python
import re
#800-555-1212
#patt = '(\(\d{3}-?\)?\d{3}-\d{4}'
patt = r'(\d{3}-|\(\d{3}\))?\d{3}-\d{4}'
phonenumber1 = "800-555-1212"
phonenumber2 = "555-1212"
phonenumber3 = "(800)555-1212"
m1 = re.match(patt,phonenumber1)
m2 = re.match(patt,phonenumber2)
m3 = re.match(patt,phonenumber3)
if m1 is not None:print m1.group()
if m2 is not None:print m2.group()
if m3 is not None:print m3.group()
print "Done"