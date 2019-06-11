valor = int(input())
n100 = valor / 100
r100 = valor % 100
n50 = r100 / 50
r50 = r100 % 50
n20 = r50 / 20
r20 = r50 % 20
n10 = r20 / 10 
r10 = r20 % 10
n5 = r10 / 5
r5 = r10 % 5
n2 = r5 / 2
r2 = r5 % 2
n1 = r2 / 1
r1 = r2 % 1
print('%d' %(valor))
print('%d nota (s) de R$ 100,00' %(n100))
print('%d nota (s) de R$ 50,00' %(n50))
print('%d nota (s) de R$ 20,00' %(n20))
print('%d nota (s) de R$ 10,00' %(n10))
print('%d nota (s) de R$ 5,00' %(n5))
print('%d nota (s) de R$ 2,00' %(n2))
print('%d nota (s) de R$ 1,00' %(n1))