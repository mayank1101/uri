sal = float(raw_input())
if sal >= 0.00 and sal <= 2000.00:
    print ('Isento')
elif sal >= 2000.01 and sal <= 3000.00:
    sal = float(sal - 2000.00)
    tax = float((8 * sal)/100.00)
    print ('R$ %.2f'%tax)
elif sal >= 3000.01 and sal <= 4500.00:
    sal = float(sal - 3000.00)
    tax = float((8 * 1000.00)/100.00) + float((18 * sal)/100.00)
    print ('R$ %.2f'%tax)
elif sal > 4500.00:
    sal = float(sal - 4500.00)
    tax = float((8 * 1000)/100.00) + float((18 * 1500)/100.00) + float((28 * sal)/100.00)
    print ('R$ %.2f'%tax)