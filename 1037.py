tempo = float(input())
if tempo >= 0 and tempo <= 25.0000:
    print('Intervalo [0,25]')
elif tempo > 25.0000 and tempo <= 50.0000:
    print('Intervalo (25,50]')
elif tempo > 50.0000 and tempo <= 75.0000:
    print('Intervalo (50,75]')
elif tempo > 75.0000 and tempo <= 100.0000:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')