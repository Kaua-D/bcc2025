entry = input().strip().split()
A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

TRIANGULO = (A*C)/2
CIRCULO = 3.14159* C**2
TRAPEZIO = (A+B)*C/2
QUADRADO = B*B
RETANGULO = A*B

print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')