'''prod1 = int(input())
prod2 = int(input())
prod = prod1 * prod2
print('PROD = %s' %(prod))'''

'''while True:
    valor = int(input())
    if valor == 2002:
        print('Acesso Permitido')
        break
    print('Senha Invalida')'''

'''num = 0
num_2 = 0
num_3 = 0
while(num < 6):
  x = float(input())
  if(x > 0):
    num_2 += 1
    num_3 += x
  num += 1
print('%d valores positivos' %num_2)
media = num_3 / num_2
print('%.1f' %media)'''

N = int(input())
for i in range(0, N):
  num = int(input())
  if num % 2 == 0 and num > 0:
    print('EVEN POSITIVE')
  elif num % 2 == 0 and num < 0:
    print('EVEN NEGATIVE')
  elif num % 2 == 1 and num > 0:
    print('ODD POSITIVE')
  elif num % 2 == 1 and num < 0:
    print('ODD NEGATIVE')
  else:
    print('NULL')