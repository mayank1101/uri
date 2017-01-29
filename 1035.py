A, B, C, D = map(int, raw_input().split(" "))
if B > C and D > A:
    if (C + D) > (A + B):
            if (C > 0 and D > 0) and (A % 2 == 0):
                print ('Valores aceitos')
            else:
            	print ('Valores nao aceitos')
    else:
    	print ('Valores nao aceitos')
else:
    print ('Valores nao aceitos')