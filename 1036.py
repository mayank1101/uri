import math
a, b, c = map(float, raw_input().split(" "))
try:
    r1 = ((-b) + (math.sqrt((b * b) - (4 * a * c))))/(2 * a)
    r2 = ((-b) - (math.sqrt((b * b) - (4 * a * c))))/(2 * a)
    print ('R1 = %.5f'%r1)
    print ('R2 = %.5f'%r2)
except:
    print ('Impossivel calcular')