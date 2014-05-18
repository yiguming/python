#!/usr/bin/python
import re
patt_day = r'(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
patt_month = r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
num_day = []
num_month = []
with open("redata1.txt",'r') as fobj:
	for item in fobj:
		num_day += re.findall(patt_day,item)
		num_month += re.findall(patt_month,item)
print num_day
print num_month
print "-"*100
print "There are %d monday in the txt file" % num_day.count("Mon")
print "There are %d Tusday in the txt file" % num_day.count("Tue")
print "There are %d Wendesday in the txt file" % num_day.count("Wed")
print "There are %d Thursday in the txt file" % num_day.count("Thu")
print "There are %d Firday in the txt file" % num_day.count("Fri")
print "There are %d Saturday in the txt file" % num_day.count("Sat")
print "There are %d Sunday in the txt file" % num_day.count("Sun")
print "-"*100
print "There are %d January in the txt file" % num_month.count("Jan")
print "There are %d February in the txt file" % num_month.count("Feb")
print "There are %d March in the txt file" % num_month.count("Mar")
print "There are %d April in the txt file" % num_month.count("Apr")
print "There are %d May in the txt file" % num_month.count("May")
print "There are %d June in the txt file" % num_month.count("Jun")
print "There are %d July in the txt file" % num_month.count("July")
print "There are %d Aguest in the txt file" % num_month.count("Aug")
print "There are %d September in the txt file" % num_month.count("Sep")
print "There are %d October in the txt file" % num_month.count("Oct")
print "There are %d November in the txt file" % num_month.count("Nov")
print "There are %d December in the txt file" % num_month.count("Dec")
print "Done!"


