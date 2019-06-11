segundos = int(input())
minutos = int(segundos / 60)
segundos -= minutos * 60
horas = int(minutos / 60)
minutos -= horas * 60
print(repr(horas)+":"+repr(minutos)+":"+repr(segundos))