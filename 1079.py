T = int(raw_input())
while T > 0:
	numsList = [float(x) for x in raw_input().split(" ")]
	avg = ((2 * numsList[0]) + (3 * numsList[1]) + (5 * numsList[2]))/(10.0)
	print ('%.1f'%avg)
	T -= 1