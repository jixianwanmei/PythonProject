import re 
line = "Cats are smartter than dogs "
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
	print "matchObj.group() : " , matchObj.group()
	print "matchObj.group(1) : " , matchObj.group(1)
	print "matchObj.group(2) : ", matchObj.group(2)
else:
	print "no match"

