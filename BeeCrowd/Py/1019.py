n = int(input())
horas = 0
minutos = 0
segundos = 0

while True:
    if n >= 3600:
        horas = n//3600
        n = n - 3600*horas

    elif n >= 60:
        minutos = n//60
        n = n- 60*minutos

    else:
        segundos = n
        break

print(f'{horas}:{minutos}:{segundos}')