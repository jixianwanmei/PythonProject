import MySQLdb

userId = raw_input("Enter your userId : ")
mIndex = int(userId)%128
str = '2016-11-01 10:13:07.280'
updateStr = 'update UserSignSystem set SignDate = ' + str + ' where UserID = ' + userId 
print updateStr
try:
    conn=MySQLdb.connect(host='172.16.10.139',user='sa',passwd='qq',db='QPAccountsDB',port=3306)
    cur=conn.cursor()
    # cur.execute(updateStr)
    # conn.commit()

    cur.execute('select * from UserSignSystem where UserID = ' + userId)

    results = cur.fetchall()

    for column in results:
    	print(column) 
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
print "operation success"