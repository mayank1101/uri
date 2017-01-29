start_date = raw_input()
start_time = raw_input()
end_date = raw_input()
end_time = raw_input()
start_Time = [x for x in start_time.split(" : ")]
end_Time = [x for x in end_time.split(" : ")]
start_Date = [x for x in start_date.split(" ")]
end_Date = [x for x in end_date.split(" ")]
days = int(end_Date[1]) - int(start_Date[1])
hr = int(end_Time[0]) - int(start_Time[0])
if hr < 0:
    hr = 24 + hr
    days -= 1
minutes = int(end_Time[1]) - int(start_Time[1])
if minutes < 0:
    minutes = 60 + minutes
    hr -= 1
sec = int(end_Time[2]) - int(start_Time[2])
if sec < 0:
    sec = 60 + sec
    minutes -= 1
print ('%d dia(s)'%days)
print ('%d hora(s)'%hr)
print ('%d minuto(s)'%minutes)
print ('%d segundo(s)'%sec)
