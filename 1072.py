N = int(raw_input())
nums = []
for _ in range(N):
	nums.append(int(raw_input()))
in_range = 0
out_range = 0
for n in nums:
    if n >= 10 and n <= 20:
        in_range += 1
    else:
        out_range += 1
print ('%d in'%in_range)
print ('%d out'%out_range)