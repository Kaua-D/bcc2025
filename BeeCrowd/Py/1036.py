#p1  Δ = b² – 4ac
#p2  x = – b ± √Δ
#       2·a
import math
entry = input().strip().split()
A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

delta = B**2 - (4*A*C)

if 2*A != 0 and delta>0:

    rdelta = math.sqrt(delta)

    x1 = (-B + rdelta)/(2*A)
    x2 = (-B - rdelta)/(2*A)

    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
else:
    print('Impossivel calcular')
