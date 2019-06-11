tab = int(input())
x = 1
while x <= 10:
    print('{0} x {1:>2} = {2:>2}'.format(x, tab, tab * x))
    x = x + 1