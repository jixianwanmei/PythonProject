import os
f1 = open('shz_Config.json')
f2 = open('shz_Config2.json','w')
for s in f1.readlines():
	f2.write(s.replace('1319138','12345678').replace('bdgw01shz_apk','new_cps_apk'))

f1.close()
f2.close()
os.remove('shz_Config.json')
os.rename('shz_Config2.json','shz_Config.json')
print 'operation success'