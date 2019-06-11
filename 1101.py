cont = 0
while cont < 1:
    x, y = map(int, input().split())
    lista = []
    if x > 0 and y > 0:
        if x < y:
            for n in range(x, y + 1):
                lista.append(n)
                resultado = ' '.join(map(str, lista))
                soma = sum(lista)
            print(resultado, 'Sum=%d' %soma)
            lista = []
        elif x > y:
            for n in range(y, x + 1):
                lista.append(n)
                resultado = ' '.join(map(str, lista))
                soma = sum(lista)
            print(resultado, 'Sum=%d' %soma)
            lista = []
    else:
        cont += 1
        