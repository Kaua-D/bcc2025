valor = float(input())
valori = valor

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0


while True:
    if valor>=100:
        n100 = n100+1
        valor = valor -100

    elif valor>=50:
        n50 = n50+1
        valor = valor -50

    elif valor>=20:
        n20 = n20+1
        valor = valor -20

    elif valor>=10:
        n10 = n10+1
        valor = valor -10

    elif valor>=5:
        n5 = n5+1
        valor = valor -5

    elif valor>=2:
        n2 = n2+1
        valor = valor -2
        
    else:
        break

print('NOTAS:')
print(int(n100),'nota(s) de R$ 100.00')
print(int(n50),'nota(s) de R$ 50.00')
print(int(n20),'nota(s) de R$ 20.00')
print(int(n10),'nota(s) de R$ 10.00')
print(int(n5),'nota(s) de R$ 5.00')
print(int(n2),'nota(s) de R$ 2.00')

n1 = 0
n050 = 0
n025 = 0
n010 = 0
n005 = 0
n001 = 0

while True:
    if valor>=1:
        n1 = n1+1
        valor = valor -1

    elif valor>= 0.5:
        n050 = n050+1
        valor = valor - 0.5

    elif valor>= 0.5:
        n025 = n025+1
        valor = valor - 0.25

    elif valor>= 0.10:
        n010 = n010+1
        valor = valor - 0.10

    elif valor>= 0.05:
        n005 = n005+1
        valor = valor - 0.05

    elif valor>= 0.01:
        n001 = n001+1
        valor = valor - 0.01
        
    else:
        break

print('MOEDAS:')
print(int(n1),'moeda(s) de R$ 1.00')
print(int(n050),'moeda(s) de R$ 0.50')
print(int(n025),'moeda(s) de R$ 0.25')
print(int(n010),'moeda(s) de R$ 0.10')
print(int(n005),'moeda(s) de R$ 0.05')
print(int(n001),'moeda(s) de R$ 0.01')