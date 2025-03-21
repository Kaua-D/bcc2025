entry = input().strip().split()
C = int(entry[0])
Q = int(entry[1])

if C == 1:
    V = Q * 4
    print(f'Total: R$ {V:.2f}')

elif C == 2:
    V = Q * 4.5
    print(f'Total: R$ {V:.2f}')

elif C == 3:
    V = Q * 5
    print(f'Total: R$ {V:.2f}')

elif C == 4:
    V = Q * 2
    print(f'Total: R$ {V:.2f}')

elif C == 5:
    V = Q * 1.5
    print(f'Total: R$ {V:.2f}')