a,b,c = map(int, raw_input().split(" "))
r = int((a + b + abs(a - b))/2)
greater = int((r + c + abs(r - c))/2)
print ('%d eh o maior' %greater)