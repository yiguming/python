#!/usr/bin/python
#-*- coding:utf-8 -*-
from __future__ import division
import UserString
import operator
import itertools


def isExactlyAString(anobj):
	if type(anobj) == type(''):
		return True
	else:
		return False

def isAstring(anobj):
	return isinstance(anobj,basestring)

def isStringLike(anobj):
	try:
		anobj.lower() + anobj + ''
	except:
		return False
	else:
		return True

astringlist = ['a','b','c']
astring = 'abc'

def pieceadd(astringlist):
	largeString4=''
	for piece in astringlist:
		largeString4 +=piece
	return  largeString4

def pieceoper(astringlist):
	largeString5 = reduce(operator.add,astringlist,'')
	return largeString5

def containAny(seq,aset):
	'''check the list seq if has the item in the aset '''
	for c in seq:
		if c in aset:return True
	return False

def containAny4(seq,aset):
	for c in seq:
		if c  not in aset:return False
	return True	

def containsAny1(seq,aset):
	for item in itertools.ifilter(aset.__contains__,seq):
		return True
	return False

def containsAny3(seq,aset):
	return bool(set(aset).isinstanction(seq))

def containsAny4(seq,aset):
	return not set(aset).difference(seq)




anumber = 123
annicode = '\u2020'
annicode1 = u'\u2020'
auserstring = UserString.UserString('abc')


print isExactlyAString(astring)
print isExactlyAString(anumber)
print isExactlyAString(annicode)
print isExactlyAString(annicode1)
print '----'


print isAstring(astring)
print isAstring(anumber)
print isAstring(annicode1)
print type(annicode1)
print type(annicode)
print 'UserString'
print isAstring(auserstring)
print isStringLike(auserstring)
print isStringLike(astring)
print isStringLike(annicode1)

x = 'xyxxyy hejyx yyx'
y = 'xyxxyy hejyxyyx'
print '|' + x.strip('xy') +'|'
print '|' + y.strip('xy') +'|'




astringtuple = ('a','b','c')
largeString = ''.join(astringlist)
largeString1 = ''.join(astringtuple)
print largeString
print largeString1

small1 = 'abc'
small2 ='bcd'
small3 = 'cde'
largeString2 = '%s%s something %s yet more' %(small1,small2,small3)
print largeString2




print pieceadd(astring)
print pieceoper(astring)



a = set('abracadabra')  
b = set('alacazam')  
     
# a包含且b包含的字符  
print a & b  
print a.intersection(b)  
# a包含或b包含的字符  
print a | b  
print a.union(b)  
# a包含且b不包含的字符  
print a - b  
print a.difference(b)  
# a包含且b不包含的字符和b包含且a不包含的字符  
print a ^ b  
print a.symmetric_difference(b) 




import string
def translator(frm='',to='',delete='',keep=None):
	if len(to) ==1:
		to = to * len(frm)
	trans = string.maketrans(frm,to)
	if keep is not None:
		allchars = string.maketrans('', '')
		delete = allchars.translate(allchars,keep.translate(allchars,delete))
	def translate(s):
		return s.translate(trans,delete)
	return translate

digits_only = translator(keep=string.digits)
print digits_only('Chris Perkins : 224-7992')
no_digits = translator(delete=string.digits)
print no_digits('Chris Perkins : 224-7992')
digits_to_hash = translator(frm=string.digits,to= '#')
print digits_to_hash('Chris Perkins :224-7992')

trans = translator(delete = 'abcd',keep ='cdef')
print trans('abcdefg')

def make_adder(addend):
	def adder(augend):return augend + addend
	return adder 

p = make_adder(23)
q = make_adder(42)
print p 
print q
print p(100)
print q(100)


import string
#生成所有字符的可复用的字符串，它还可以作为一个翻译表，指明“无须翻译”
allchars = string.maketrans('','')
def makefilter(keep):
	"""
	返回一个函数，此返回函数接受一个字符串为参数并返回字符串的一个部分拷贝，此拷贝只包含在
	keep 中的字符，注意keep 必须是一个普通字符串
	"""
	
#生成一个由所有不在keep中的字符组成的字符串：keep的补集，既所有我们需要删除的字符
	delchars = allchars.translate(allchars,keep)
	def thefilter(s):
		return s.translate(allchars,delchars)
	return thefilter
if __name__ == '__main__':
	just_vowels = makefilter('aeiouy')
	print just_vowels('four score and seven years ago')
	print just_vowels('tiger,tiger burning bright')

print makefilter.__doc__



import sets
class Keeper(object):
	def __init__(self,keep):
		self.keep = sets.Set(map(ord,keep))
	def __getitem__(self,n):
		if n not in self.keep:
			return None
		return unichr(n)
	def __call__(self,s):
		return unicode(s).translate(self)
makefilter = Keeper
if __name__ == '__main__':
	just_vowels = makefilter('aeiouy')
	print just_vowels(u'four score and seven years ago')
	print just_vowels(u'tiger,tiger burning bright')


import string
text_characters = "".join(map(chr,range(32,127))) + "\n\r\t\b"
_null_trans = string.maketrans("","")
def istext(s,text_characters=text_characters,threshold=0.30):
	#若s包含了空值，它不是文本
	if "\0" in s:
		return False
	#一个 “空”字符串是“文本”(这是一个主观但又很合理的选择)
	if not s:
		return True
	# 获得s的由非文本字符构成的字串
	t = s.translate(_null_trans,text_characters)
	# 如果不超过30%的字符是非文本字符，s是字符串
	return len(t)/len(s) <=threshold

def istexfile(filename,blocksize=512,**kwds):
	return istext(open(filename).read(blocksize),**kwds)

litter = "abc"
big = litter.upper()
print big
big1 = "def"
little = big.lower()
print little

astring = 'one tWo thrEe'
print astring.capitalize()
print astring[:1].upper()+astring[1:].lower()
print astring.title()


def iscapitalize(s):
	return s == s.capitalize()

print iscapitalize('One two three')
#空字符串和
print iscapitalize('')
print iscapitalize('123')


import string
notrans = string.maketrans('','') #identity''translation''
def containsAny(str,strset):
	return len(strset) != len(strset.translate(notrans,str))
def iscapitalized(s):
	return s == s.capitalize() and containsAny(s,string.letters)

print iscapitalized('One two three')
print iscapitalized('')
print iscapitalized('123')

theline = "0123456789"
thelongline = "123456789012345678901234567890"
afield = theline[3:8]
print afield



import struct 
baseformat = "5s 3x 8s 8s"
print struct.calcsize(baseformat)
numremain = len(thelongline) -struct.calcsize(baseformat)
print numremain
format = "%s %ds" %(baseformat,numremain)
print format
l,s1,s2,t = struct.unpack(format,thelongline)
print l,s1,s2,t
#如果想跳过“其余部分”，只需要给出正确的长度，拆解出theline的开头部分的数据即可
l,s1,s2 = struct.unpack(baseformat,thelongline[:struct.calcsize(baseformat)])
print l,s1,s2

#5字节一组的数据
fivers = [thelongline[k:k+5] for k in xrange(0,len(thelongline),5)]
print fivers

chars = list(thelongline)
print chars

cuts = [8,14,20,26,30]
pieces = [thelongline[i:j] for i,j in zip([0]+cuts,cuts+[None])]
print zip([0]+cuts,cuts+[None])
print pieces


def fields(baseformat,theline,lastfield =False):
	numremain = len(theline) -struct.calcsize(baseformat)
	format = "%s %ds" %(baseformat,numremain,lastfield and "s" or "x")
	return struct.unpack(format,theline)

#memoizing mode fields version
def fields_momoizing(baseformat,theline,lastfield=False,_cache={}):
	#生成键并尝试获得缓存的格式字符串
	key = baseformat,len(theline),lastfield
	format = _cache.get(key)
	if format is None:
		#没有缓存的格式字符串，创建并缓存之
		numremain  = len(theline) -struct.calcsize(baseformat)
		_cache[key] = format = "%s %d%s" % (baseformat,numremain,lastfield and "s" or "x")
	return struct.unpack(format,theline)


def split_by(theline,n,lastfield =False):
	#切割所有需要的片段
	pieces = [theline[k:k+n] for k in xrange(0,len(theline),n)]
	#若最后一段太短或不需要，丢弃之
	if not lastfield and len(pieces[-1]) < n :
	    pieces.pop()
	return pieces

def split_at(theline,cuts,lastfield=False): 
	pieces = [theline[i:j] for i,j in zip([0]+cuts,cuts+[None])]
	if not lastfield:
		pieces.pop()
	return pieces

def split_at_yield(the_line,cuts,lastfield=False):
	last = 0
	for cut in cuts:
		yield the_line[last:cut]
		last = cut
	if lastfield:
		yield the_line[last:]

def split_by2(the_line,n,lastfield=False):
	return split_at(the_line,xrange(n,len(the_line),n),lastfield)



#1.14
def reindent(s,numSpaces):
	leading_space = numSpaces * ' '
	lines = [leading_space + line.strip() for line in s.splitlines()]
	#print line 
	#print s.splitlines()
	#print line.strip()
	#print lines
	return '\n'.join(lines)

x = """     line one
	line two
           and line three 
"""
print x

print reindent(x,4)



def addSpaces(s,numAdd):
	white = " " *numAdd
	return white + white.join(s.splitlines(True))
def numSpaces(s):
	return [len(line) - len(line.lstrip()) for line in s.splitlines()]
def delSpaces(s,numDel):
	if numDel > min(numSpaces(s)):
		raise ValueError,"removeing more spaces than there are!"
	return '\n'.join([line[numDel:] for line in s.splitlines()])
def unIndentBlock(s):
	return delSpaces(s,min(numSpaces(s)))
print "-"*10
print unIndentBlock(x)
print x 














