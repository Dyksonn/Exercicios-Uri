dia = int(input().split()[1])
hora = input().split(':')
hi = int(hora[0])
minuto = int(hora[1])
segundo = int(hora[2])

dfinal = int(input().split()[1])

hora = input().split(':')
hf = int(hora[0])
mfinal = int(hora[1])
sfinal = int(hora[2])

dias = dfinal - dia 

horas = hf - hi

if horas < 0:
    horas += 24
    dias -= 1
minutos = mfinal - minuto
if minutos < 0:
    minutos += 60
    horas -= 1
segundos = sfinal - segundo
if segundos < 0:
    segundos += 60
    minutos -= 1
print('%d dia(s)' %dias)
print('%d hora(s)' %horas)
print('%d minuto(s)' %minutos)
print('%d segundo(s)' %segundos)