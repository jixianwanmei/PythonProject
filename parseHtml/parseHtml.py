#coding:utf-8
#!/usr/bin/python
#!/usr/local/lib/python2.7/site-packages
import sys
import re
import random
from bs4 import BeautifulSoup,Tag,CData
reload(sys)
sys.setdefaultencoding('utf8')
soup = BeautifulSoup(open('article1.html'))
# contents = soup.a.font.contents
# str_convert = ''.join(contents)
# print str_convert
# print type(contents)
# print soup.a.font
def list2str(list):
	content='%s'*len(list) % tuple(list) 
	# print(content)
	dr = re.compile(r'<[^>]+>',re.S)
	dd = dr.sub('',content)
	return ("".join(dd.split()))

# list = soup.findAll('a',{'class':'fz14'})

# for x in list :
# 	# print(type(x.contents))
# 	ac = x.contents
# 	content='%s'*len(ac) % tuple(ac) 
# 	# print(content)
# 	dr = re.compile(r'<[^>]+>',re.S)
# 	dd = dr.sub('',content)
# 	print dd

# list2 = soup.findAll('td',{'class':'author_flag'})
# for x in list2:
# 	print(list2str(x.contents))
# list3= soup.findAll('td',{'class':'cjfdyxyz'})

# for x in list3:
# 	print(list2str(x.contents))

list = soup.findAll('tr')
for i in range(1,len(list)):
	author = list2str(list[i].contents[4])
	article = list2str(list[i].contents[2])
	magazine = list2str(list[i].contents[6])
	time = list2str(list[i].contents[8])
	page = int(random.randint(10,99)) 
	page2 = int(page+random.randint(2,5))
	pageStr1 = str(page)
	pageStr2 = str(page2)
	pageStr = pageStr1+'-'+pageStr2
	res = '['+str(i)+']'+ author+'.'+article+'[J].' +magazine+','+time+':'+pageStr
	print(res)


