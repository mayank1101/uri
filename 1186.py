row,arr,s,avg,count = [],[],0,0,0
opt = raw_input()
for i in range(12):
	for j in range(12):
		row.append(float(raw_input()))
	arr.append(row)
	row = []
if opt == 'S':
	for i in range(1,12):
		for j in range(11,11-i,-1):
			s += arr[i][j]
	print s
else:
	for i in range(1,12):
		for j in range(11,11-i,-1):
			avg,count = avg + arr[i][j],count + 1
	print ('%.1f'%((avg)/float(count)))
