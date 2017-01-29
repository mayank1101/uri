nums = []
for i in range(1,101):
	nums.append(int(raw_input()))
print (max(nums))
ind = nums.index(max(nums))
print (ind + 1)