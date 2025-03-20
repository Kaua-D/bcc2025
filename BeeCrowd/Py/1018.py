valor = int(input())

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

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

    elif valor>=1:
        n1 = n1+1
        valor = valor -1

    else:
        break

print(n100,'nota(s) de R$ 100,00')
print(n50,'nota(s) de R$ 50,00')
print(n20,'nota(s) de R$ 20,00')
print(n10,'nota(s) de R$ 10,00')
print(n5,'nota(s) de R$ 5,00')
print(n2,'nota(s) de R$ 2,00')
print(n1,'nota(s) de R$ 1,00')