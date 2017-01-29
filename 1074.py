N = int(raw_input())
nums = []
for x in range(N):
    nums.append(int(raw_input()))
    if nums[x] == 0:
        print ('NULL')
    elif nums[x] > 0:
        if nums[x] % 2 == 0:
            print ('EVEN POSITIVE')
        else:
            print ('ODD POSITIVE')
    else:
        if nums[x] % 2 == 0:
            print ('EVEN NEGATIVE')
        else:
            print ('ODD NEGATIVE')
