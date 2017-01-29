l = [float(x) for x in raw_input().split(" ")]
l1 = sorted(l, reverse = True)
if l1[0] >= (l1[1] + l1[2]):
    print ('NAO FORMA TRIANGULO')
else:
    if (l1[0]**2) == (l1[1]**2 + l1[2]**2):
        print ('TRIANGULO RETANGULO')
    elif (l1[0]**2) > (l1[1]**2 + l1[2]**2):
        print ('TRIANGULO OBTUSANGULO')
    elif (l1[0]**2) < (l1[1]**2 + l1[2]**2):
        print ('TRIANGULO ACUTANGULO')
    if (l1[0] == l1[1] == l1[2]):
        print ('TRIANGULO EQUILATERO')
    else:
        if (l1[0] == l1[1]) and (l1[0] != l1[2]) and (l1[1] != l1[2]):
            print ('TRIANGULO ISOSCELES')
        elif (l1[0] == l1[2]) and (l1[0] != l1[1]) and (l1[2] != l1[1]):
            print ('TRIANGULO ISOSCELES')
        elif (l1[1] == l1[2]) and (l1[1] != l1[0]) and (l1[2] != l1[0]):
            print ('TRIANGULO ISOSCELES')