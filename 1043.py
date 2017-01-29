a,b,c = map(float, raw_input().split(" "))
r = (a + b + abs(a -b))/2
longest = (r + c + abs(r -c))/2
if (longest == a) and (b + c > a):
    print ('Perimetro = %.1f'%(a + b + c))
elif (longest == b) and (a + c > b):
    print ('Perimetro = %.1f'%(a + b + c))
elif (longest == c) and (a + b > c):
    print ('Perimetro = %.1f'%(a + b + c))
else:
    print ('Area = %.1f'%((1/2.0)*(a + b) * c))