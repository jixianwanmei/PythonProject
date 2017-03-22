a = "../file/file2/file3"
b = "../file_c"
arr = a.split("/")

c =""
for num in range(2,len(arr)):
	c = c+"/"+arr[num]

c = b+c
print c