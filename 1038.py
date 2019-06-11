codigo, quantidade = input().split(" ")
codigo = int(codigo)
quantidade = int(quantidade)
if codigo == 1:
    preço = 4.0 * quantidade
elif codigo == 2:
    preço = 4.5 * quantidade
elif codigo == 3:
    preço = 5 * quantidade
elif codigo == 4:
    preço = 2 * quantidade 
elif codigo == 5:
    preço = 1.5 * quantidade
print('Total: R$ %.2f' %preço)