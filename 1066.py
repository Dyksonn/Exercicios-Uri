n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
lista = [n1, n2, n3, n4, n5]
n = 0
pares = 0
impares = 0
positivo = 0 
negativo = 0
while n < len(lista):
    if lista[n] % 2 == 0:
        pares += 1
    elif lista[n] % 2 != 0:
        impares += 1
    if lista[n] > 0:
        positivo += 1
    elif lista[n] < 0:
        negativo += 1
    n += 1
print("%d valor(es) par(es)" %pares)
print("%d valor(es) impar(es)" %impares)
print("%d valor(es) positivo(s)" %positivo)
print("%d valor(es) negativo(s)" %negativo)

