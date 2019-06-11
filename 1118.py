'''x = 0
y = 0
while True:
    notas = float(input())
    if notas >= 0 and notas <= 10:
        x += 1
        y += notas
        if x == 2:
            print('media = %.2f' %(y/2))
            novo = int(input('novo calculo (1-sim 2-nao)'))
            if novo == 1:
                continue
            elif novo == 2:
                break
            else:
                novo = int(input('novo calculo (1-sim 2-nao)'))
    else:
        print('nota invalida')'''

x=0
c=0
while True:
  notas=float(input())
  if notas >= 0 and notas <= 10:
    x+=1
    c+=notas
    if x == 2:
      print("media = %.2f" % (c/2))
      novo=int(input("novo calculo (1-sim 2-nao)"))
      if novo == 1:
        continue
      elif novo == 2:
        break
      else:
        novo=int(input("novo calculo (1-sim 2-nao)"))
  else:
    print("nota invalida")