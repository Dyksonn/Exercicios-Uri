numero = int(input())
for i in range(numero):
    linha = [int(n) for n in input().split(' ')]
    x = min(linha)
    y = max(linha)
    soma = 0
    for n in range(x+1,y):
        if n % 2 == 1:
            soma += n 
    print(soma)