x = int(raw_input())
k = 0
while k != 6:
    if (x + 1) % 2 != 0:
        print (x + 1)
        k += 1
        x += 2
    else:
        print (x+2)
        k += 1
        x += 2