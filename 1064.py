num = 0
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
print('%.1f' %media)