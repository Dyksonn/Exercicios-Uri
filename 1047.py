entrada = [int(i) for i in input().split(' ')]
hora = entrada[0]
minuto = entrada[1]
horafi = entrada[2]
minutofi = entrada[3]
total = horafi - hora
if total < 0:
    total += 24
minuto_total = minutofi - minuto
if minuto_total < 0:
    minuto_total += 60
    total -= 1
if minuto_total == 0 and total == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(total, minuto_total))