valor = input().split(" ")
a = float(valor[0])
b = float(valor[1])
c = float(valor[2])

if (a < b + c) and (b < a + c) and (c < a + b):
    perimetro = a + b + c
    print('Perimetro = %.1f' %perimetro)
else:
    area = ((a + b)* c) / 2
    print('Area = %.1f' %area) 