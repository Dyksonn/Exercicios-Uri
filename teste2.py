def Entrada():
    global lista, entry

    print("Quantos itens nessa lista?")

    entry = int(input())

    print("Escreva os itens:")
    
    x = 1
    lista = []
    while x <= entry:
        lista.append(input())
        x = x + 1
Entrada()

print('Numero de itens:', entry)



print(lista)
print("Deseja Adicionar mais algum item? S/N")

choice = str(input())

if(choice == "S" or choice == "s"):
    print("Quantos Elementos?")
    entry = int(input())

    print("Digite os itens à adicionar:")
    
    x = 1
    lista2 = []
    while x <= entry:
        lista2.append(input())
        x = x + 1
    print(lista + lista2)

elif(choice == "N" or choice == "n"):
    print(lista)
print("Okay, Fim do codigo...")