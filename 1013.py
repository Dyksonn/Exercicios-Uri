import math
linha1 = input().split(" ")
a, b, c = linha1
a = int(a)
b = int(b)
c = int(c)
maior = (a + b + abs(a - b))/2
resultado = (maior + c + abs(maior - c))/2
print("%d eh o maior" %(resultado))