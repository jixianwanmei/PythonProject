#coding:utf-8
import os
#标准类型内建函数
#1.type
print (type(4))
print type('hello world')
print type(type(4))
#<type 'int'>
#<type 'str'>
#<type 'type'>
#2.cmp()--->根据字面意思是compare的意思
a , b = 4,12
print cmp(a,b)
# -1
print cmp(b,a)
# 1
b = 4
print cmp(a,b)
# 0 equal print 0 
c,d = 'abc','xyz'
print cmp(c,d)
#3.str()和 repr() 及''操作符
a = 4.53-2j
b = 1 
c = 2e10
d = [1,2,3,4]
print str(a)  
print str(b)
print str(c)
print str(d)
#
# (4.53-2j)
# 1
# 20000000000.0
# [1, 2, 3, 4]
print repr(a)  
print repr(b)
print repr(c)
print repr(d)
#
# (4.53-2j)
# 1
# 20000000000.0
# [1, 2, 3, 4]
# str()函数获得的字符串可读性好，repr一般是用来重新获得对像的值 obj ==eval(repr(obj))这个等式是成立的；
