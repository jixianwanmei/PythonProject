#! /usr/bin/env python
'readTextFile.py --read and display text file '
#get filename
import os 
ls = os.linesep
fname = 'DZGameView.lua'

# attempt to open file for reading 

try:
	fobj = open(fname,'r')
except IOError,e:
	print "*** file open error:",e
else:
	for eachLine in fobj:
		print eachLine,
		
	fobj.close()
