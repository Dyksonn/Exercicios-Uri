linha1 = input().split(" ")
A,B,C,D = linha1
A = int(A)
B = int(B)
C = int(C)
D = int(D)
if B > C and D > C and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')