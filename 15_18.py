#/usr/bin/python
import re
from time import strptime
from time import mktime
patt =r'(.+)::.+::(\d+)'
with open('redatatest.txt','r') as f:
	for line in f:
		m = re.match(patt,line)
		if m is not None:print m.group(1),m.group(2)
		time1=mktime(strptime(m.group(1)))
		time2 = float(m.group(2))
		if time1 == time2:
			print "Matched"
		else:
			print "Don't macth"
