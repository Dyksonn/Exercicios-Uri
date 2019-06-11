entrada = input().split(" ")
valor = [int(i) for i in entrada]
valor.sort()
print(*valor,sep='\n')
print()
print(*entrada,sep='\n')