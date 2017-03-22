#!/usr/bin/env python
'makeTextFile.py -- create text file'
import os 
ls = os.linesep
#get file name 
while True:
	fname = raw_input('Enter a fileName : ')
	if os.path.exists(fname):
		print 'already exists'
	else:
		break
all = []
print "\nEnter lines ('.' by iteself to quit ).\n"
while True:
	entry = raw_input('>')
	if entry == '.':
		break
	else:
		all.append(entry)

#write lines to file with proper line-ending 
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE'