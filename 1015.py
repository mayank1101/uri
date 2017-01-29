from math import sqrt
x1, y1 = map(float, raw_input().split(" "))
x2, y2 = map(float, raw_input().split(" "))
dis = float(sqrt((((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))))
print ('%.4f' %dis)