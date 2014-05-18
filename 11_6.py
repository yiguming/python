#!/usr/bin/python
a = 'abc'
print "%s" % a 

def printf(fmt,*args):
	print fmt % args

if __name__ == '__main__':
	printf('%s','tom')
	printf('%d',12)
	printf('%f',12)

print '%s' % 'tom'
print '%d' % 12
print '%f' % 12
