N = int(raw_input())
sampleList = []
for i in range(N):
    sample = [x for x in raw_input().split(" ")]
    sampleList.append(sample)
coelho = 0
rato = 0
sapo = 0
for amount, type in sampleList:
    if type == 'C':
        coelho += int(amount)
    elif type == 'R':
        rato += int(amount)
    elif type == 'S':
        sapo += int(amount)

tot = coelho + rato + sapo
print ('Total: %d cobaias' % tot)
print ('Total de coelhos: %d' % coelho)
print ('Total de ratos: %d' % rato)
print ('Total de sapos: %d' % sapo)
print ('Percentual de coelhos: %.2f' % float((coelho * 100) / float(tot)) + ' %')
print ('Percentual de ratos: %.2f' % float((rato * 100) / float(tot)) + ' %')
print ('Percentual de sapos: %.2f' % float((sapo * 100) / float(tot)) + ' %')