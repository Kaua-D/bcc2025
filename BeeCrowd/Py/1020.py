d = int(input())
ano = 0
mes = 0
dias = 0

while True:
    if d >= 365:
        ano = d//365
        d = d - 365*ano

    elif d >= 30:
        mes = d//30
        d = d - 30*mes

    else:
        dias = d
        break

print(ano,'ano(s)')
print(mes,'mes(es)')
print(dias,'dia(s)')