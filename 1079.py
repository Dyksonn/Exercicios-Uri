numero = int(input())
lista = []
for n in range(numero):
    valores = input()
    valores = valores.split()
    n1 = float(valores[0])
    n2 = float(valores[1])
    n3 = float(valores[2])
    lista.append((n1 * 2 + n2 * 3 + n3 * 5) / 10)
for n in range(numero):
    print('%.1f' %(lista[n]))
