idade = int(input())
anos = idade / 365
mês = (idade % 365) / 30
dias = (idade % 365) % 30
print('%d ano(s)' %(anos))
print('%d mes(es)' %(mês))
print('%d dia(s)' %(dias))