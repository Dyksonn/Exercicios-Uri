x, y = map(int, input().split())
cont = 1
cont2 = 0
soma = ""
while cont < y:
    while cont2 < x:
        soma = soma + str(cont) + " "
        if cont == y:
            cont2 = x
        cont += 1
        cont2 += 1
    cont2 = 0
    print(soma[0:-1])
    soma = ""