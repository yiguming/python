#!/usr/bin/env python
import re
patt = r'(\w+) (\w+) \d\d \d\d:\d\d:\d\d\s+\d\d\d\d' 
mon,tue,wed,thu,fri,sat,sun =0,0,0,0,0,0,0
jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec=0,0,0,0,0,0,0,0,0,0,0,0
with open("redata1.txt") as fobj1:
    for item in fobj1:
        m = re.match(patt,item)
        if m is not None:print m.group(1),m.group(2)
        if m.group(1) =='Mon':mon +=1
    	elif m.group(1) =='Tue':tue +=1
    	elif m.group(1) =='Wed':wed +=1
    	elif m.group(1) =='Thu':thu +=1
    	elif m.group(1) =='Fri':fri +=1
    	elif m.group(1) =='Sat':sat +=1
    	elif m.group(1) =='Sun':sun +=1 
        if m.group(2) =='Jan':jan +=1
    	elif m.group(2)=='Feb':feb +=1
    	elif m.group(2)=='Mar':mar +=1
    	elif m.group(2)=='Apr':apr +=1
    	elif m.group(2)=='May':may +=1
    	elif m.group(2)=='Jun':jun +=1
    	elif m.group(2)=='Jul':jul +=1
    	elif m.group(2)=='Aug':aug +=1
    	elif m.group(2)=='Sep':sep +=1
    	elif m.group(2)=='Oct':octo +=1
    	elif m.group(2)=='Nov':nov +=1
    	elif m.group(2)=='Dec':dec +=1
print "The day in the txt file"
print "There are %d monday in the txt file" % mon
print "There are %d Tusday in the txt file" % tue
print "There are %d Wendesday in the txt file" % wed
print "There are %d Thursday in the txt file" % thu
print "There are %d Firday in the txt file" % fri
print "There are %d Saturday in the txt file" % sat
print "There are %d Sunday in the txt file" % sun
print "-"*100
print "The month in the txt file"
print "There are %d January in the txt file" % jan
print "There are %d February in the txt file" % feb
print "There are %d March in the txt file" % mar
print "There are %d April in the txt file" % apr
print "There are %d May in the txt file" % may
print "There are %d June in the txt file" % jun
print "There are %d July in the txt file" % jul
print "There are %d Aguest in the txt file" % aug
print "There are %d September in the txt file" % sep
print "There are %d October in the txt file" % octo
print "There are %d November in the txt file" % nov
print "There are %d December in the txt file" % dec
print 'Done'
