import os
def doWork():
	f1 = open('SHZCommands.ts')
	f2 = open('SHZCommands2.ts','w')
	for s in f1.readlines():
		if s.find('//')!=-1 and len(s.split('//'))!=0:
			# f2.write(s.replace())
			print(s)
			print('-----------')
			str2 = s.split('//')
			print('/**' + str2[1] + '*/')
			f2.write('/**' + str2[1].rstrip() + '*/' + '\n')
			f2.write(str2[0] + '\n')
		else:
			f2.write(s)
	f1.close()
	f2.close()
	os.remove('SHZCommands.ts')
	os.rename('SHZCommands2.ts','SHZCommands.ts')

doWork()