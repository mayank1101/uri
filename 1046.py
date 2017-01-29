tart, end = map(int, raw_input().split(" "))
if start == end:
    tot = 24
    print ('O JOGO DUROU %d HORA(S)'%tot)
else:
    if start > 12 and end < 12:
        tot = (24 % start) + end
        print ('O JOGO DUROU %d HORA(S)'%tot)
    elif start < 12 and end > 12:
        tot = end - start
        print ('O JOGO DUROU %d HORA(S)'%tot)
    elif start > 12 and end > 12:
        tot = (24 - (24 % start)) + (24 - (24 % end))
        print ('O JOGO DUROU %d HORA(S)'%tot)