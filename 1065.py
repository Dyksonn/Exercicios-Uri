par = 0
x = 1 
while x <= 5:
    n = int(input())
    if (n % 2 == 0):
        par = par + 1
    x = x + 1
print('%d valores pares' %par)