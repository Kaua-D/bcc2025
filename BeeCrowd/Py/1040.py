entry = input().strip().split()
n1 = float(entry[0])
n2 = float(entry[1])
n3 = float(entry[2])
n4 = float(entry[3])

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10
print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')

elif media < 5:
    print('Aluno reprovado.')

else:
    print('Aluno em exame.')
    
    exame = float(input())
    print('Nota do exame:', exame)

    medfin = (exame + media)/2

    if medfin >= 5:
        print('Aluno aprovado.')

    else:
        print('Aluno em exame.')

    print(f'Media final: {medfin:.1f}')