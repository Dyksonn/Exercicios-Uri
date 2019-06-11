notas = input().split(" ")
n1, n2, n3, n4 = notas
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
Media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print('Media: %0.1f' %Media)
if Media >= 7.0:
    print('Aluno aprovado.')
elif Media >= 5.0:
    print('Aluno em exame.')
    exame = input()
    exame = float(exame)
    nota2 = (Media + exame) / 2
    if nota2 >= 5:
        print('Nota do exame: %0.1f' %exame)
        print('Aluno aprovado.')
        print('Media final: %0.1f' %nota2)
    else:
        print('Nota do exame: %0.1f' %exame)
        print('Aluno reprovado.')
        print('Media final: %0.1f' %nota2)
else:
    print('Aluno reprovado.')
 