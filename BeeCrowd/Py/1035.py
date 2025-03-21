entry = input().strip().strip().split()
A = int(entry[0])
B = int(entry[1])
C = int(entry[2])
D = int(entry[3])

if (B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

'''
Esse foi a base para a simplificação atual.

if B>C and D>A:
    if C+D > A+B:
        if C>0 and D>0:
            if A%2 == 0:
                print('Valores aceitos')
            
            else:
                ('Valores nao aceitos')

        else:
            ('Valores nao aceitos')
    
    else:
        print('Valores nao aceitos')

else:
    print('Valores nao aceitos')
'''