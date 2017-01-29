amount = int(raw_input())
print (amount)
n_of_hun = int(amount/100)
print('%d nota(s) de R$ 100,00'%n_of_hun)
amount %= 100
n_of_fifty = int(amount/50)
print('%d nota(s) de R$ 50,00'%n_of_fifty)
amount %= 50
n_of_twenty = int(amount/20)
print('%d nota(s) de R$ 20,00'%n_of_twenty)
amount %= 20
n_of_ten = int(amount/10)
print('%d nota(s) de R$ 10,00'%n_of_ten)
amount %= 10
n_of_five = int(amount/5)
print('%d nota(s) de R$ 5,00'%n_of_five)
amount %= 5
n_of_two = int(amount/2)
print('%d nota(s) de R$ 2,00'%n_of_two)
amount %= 2
n_of_one = int(amount/1)
print('%d nota(s) de R$ 1,00'%n_of_one)