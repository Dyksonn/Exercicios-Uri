numero = int(input())
dentro = 0 
fora = 0 
for i in range (numero):
    num = int(input())
    if 10 <= num <= 20:
        dentro += 1
    else:
        fora += 1
print('%d in' %dentro)
print('%d out' %fora)