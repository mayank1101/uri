time = int(raw_input())
n_of_hr = time/3600
time %= 3600
n_of_min = time/60
time %= 60
n_of_sec = time
print ('%d:%d:%d'%(n_of_hr, n_of_min, n_of_sec))