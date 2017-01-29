nums = []
n1 = float(raw_input())
nums.append(n1)
n2 = float(raw_input())
nums.append(n2)
n3 = float(raw_input())
nums.append(n3)
n4 = float(raw_input())
nums.append(n4)
n5 = float(raw_input())
nums.append(n5)
n6 = float(raw_input())
nums.append(n6)
pos = 0
avg = 0
for x in nums:
    if x > 0:
        pos += 1
        avg += x
print ('%d valores positivos'%pos)
print ('%.1f'%float(avg/pos))