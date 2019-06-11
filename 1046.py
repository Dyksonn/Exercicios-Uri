horas = input().split(" ")
hora1 = int(horas[0])
hora2 = int(horas[1])
if hora1 == hora2:
    print('O JOGO DUROU 24 HORA(S)')
else:
    hora = hora2 - hora1
    if(hora < 0):
        hora += 24
    print('O JOGO DUROU %d HORA(S)' %hora)