linha1 = input().split(" ")
linha2 = input().split(" ")
peca1,quantidade1,valor1 = linha1
peca2,quantidade2,valor2 = linha2
peca1 = int(peca1)
quantidade1 = int(quantidade1)
peca2 = int(peca2)
quantidade2 = int(quantidade2)
valor1 = float(valor1)
valor2 = float(valor2)
pagar = (quantidade1 * valor1) + (quantidade2 * valor2)
print('VALOR A PAGAR: R$ %.2f' %(pagar))


 