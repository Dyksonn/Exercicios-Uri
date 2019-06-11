valor = 0
alcool = 0 
gasolina = 0
diesel = 0
while valor != 4:
    valor = int(input())
    if valor == 1:
        alcool += 1
    if valor == 2:
        gasolina += 1
    if valor == 3:
        diesel += 1
print('MUITO OBRIGADO')
print('Alcool: %d' %alcool)
print('Gasolina: %d' %gasolina)
print('Diesel: %d' %diesel)