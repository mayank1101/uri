code, quantity = map(int, raw_input().split(" "))
if code == 1:
    amount = float(quantity * 4.00)
    print ('Total: R$ %.2f'%amount)
elif code == 2:
    amount = float(quantity * 4.50)
    print ('Total: R$ %.2f'%amount)
elif code == 3:
    amount = float(quantity * 5.00)
    print ('Total: R$ %.2f'%amount)
elif code == 4:
    amount = float(quantity * 2.00)
    print ('Total: R$ %.2f'%amount)
elif code == 5:
    amount = float(quantity * 1.50)
    print ('Total: R$ %.2f'%amount)