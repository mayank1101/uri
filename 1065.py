n1, n2, n3, n4, n5 = int(raw_input()), int(raw_input()), int(raw_input()), int(raw_input()), int(raw_input())
nums = []
nums.append(n1)
nums.append(n2)
nums.append(n3)
nums.append(n4)
nums.append(n5)
even = 0
for n in nums:
    if n % 2 == 0:
        even += 1
print ('%d valores pares'%even)