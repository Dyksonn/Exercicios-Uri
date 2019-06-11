linha1 = input().split(" ")
A,B,C = linha1
A = float(A)
B = float(B)
C = float(C)
tri = A * C /2
cir = 3.14159 * pow(C,2)
tra = ((A + B)*C)/2
qua = B * B
reta = A * B
print('TRIANGULO: %.3f' %(tri))
print('CIRCULO: %.3f' %(cir))
print('TRAPEZIO: %.3f' %(tra))
print('QUADRADO: %.3f' %(qua))
print('RETANGULO: %.3f' %(reta))