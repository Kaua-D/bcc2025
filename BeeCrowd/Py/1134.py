al, ga, di = 0,0,0
while True:
    n = int(input())
    if n == 1:
        al= al+1

    elif n == 2:
        ga= ga+1

    elif n == 3:
        di = di +1

    elif n == 4:
        break

print('MUITO OBRIGADO')
print('Alcool:', al)
print('Gasolina:',ga)
print('Diesel:',di)