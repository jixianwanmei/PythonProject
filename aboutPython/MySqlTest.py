
import MySQLdb

userId = raw_input("Enter your userId : ")
score = raw_input("Enter Score that you wish to update : ")

mIndex = int(userId)%128
updateStr = 'update accountsinfo_'+str(mIndex)+'  set Score = ' + score + ' where userId = ' + userId 
print updateStr
try:
    conn=MySQLdb.connect(host='172.16.10.222',user='root',passwd='qq',db='qpaccountsdb',port=3306)
    cur=conn.cursor()
    cur.execute(updateStr)
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])