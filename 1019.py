age = int(raw_input())
n_of_years = age/365
print ('%d ano(s)' % n_of_years)
age = age % 365
n_of_months = age/30
print ('%d mes(es)' % n_of_months)
age %= 30
n_of_days = age
print ('%d dia(s)' % n_of_days)