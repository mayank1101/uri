sal = float(raw_input())
if sal >= 0 and sal <= 400.00:
    new_sal = sal + ((15 * sal)/100.0)
    inc = new_sal - sal
    per = '15 %'
    print ('Novo salario: %.2f'%new_sal)
    print ('Reajuste ganho: %.2f'%inc)
    print ('Em percentual: '+per)
elif sal >= 400.01 and sal <= 800.00:
    new_sal = sal + ((12 * sal)/100.0)
    inc = new_sal - sal
    per = '12 %'
    print ('Novo salario: %.2f'%new_sal)
    print ('Reajuste ganho: %.2f'%inc)
    print ('Em percentual: '+per)
elif sal >= 800.01 and sal <= 1200.00:
    new_sal = sal + ((10 * sal)/100.0)
    inc = new_sal - sal
    per = '10 %'
    print ('Novo salario: %.2f'%new_sal)
    print ('Reajuste ganho: %.2f'%inc)
    print ('Em percentual: '+per)
elif sal >= 1200.01 and sal <= 2000.00:
    new_sal = sal + ((7 * sal)/100.0)
    inc = new_sal - sal
    per = '7 %'
    print ('Novo salario: %.2f'%new_sal)
    print ('Reajuste ganho: %.2f'%inc)
    print ('Em percentual: '+per)
else:
    new_sal = sal + ((4 * sal)/100.0)
    inc = new_sal - sal
    per = '4 %'
    print ('Novo salario: %.2f'%new_sal)
    print ('Reajuste ganho: %.2f'%inc)
    print ('Em percentual: '+per)