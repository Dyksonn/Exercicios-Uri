valor = []
soma = 0
valor.append(float(input()))
valor.append(float(input()))
valor.append(float(input()))
valor.append(float(input()))
valor.append(float(input()))
valor.append(float(input()))
for n in valor:
    if (float (n) > 0):
        soma = soma + 1
print(soma,'valores positivos')
