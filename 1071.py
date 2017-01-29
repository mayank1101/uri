x, y = int(raw_input()), int(raw_input())
sum = 0
if (x > 0 and y > 0) or (x < 0 and y < 0):
	if x > y:
		for n in range(y+1,x):
			if n % 2 != 0:
				sum += n
	elif x < y:
		for n in range(x+1,y):
			if n % 2 != 0:
				sum += n
elif x < 0 and y > 0:
    for n in range(x+1,y):
        if n % 2 != 0:
            sum += n
elif x > 0 and y < 0:
    for n in range(y+1,x):
        if n % 2 != 0:
            sum += n
print (sum)