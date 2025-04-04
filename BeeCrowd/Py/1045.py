entry = input().strip().split()
A = float(entry[0])
B = float(entry[1])
C = float(entry[2])

if A>0 and B>0 and C>0:

    if A>B and A>C:
        if B>C:
            m1 = A
            m2 = B
            m3 = C

        else:
            m1 = A
            m2 = C
            m3 = B

    elif B>A and B>C:
        if A>C:
            m1 = B
            m2 = A
            m3 = C

        else:
            m1 = B
            m2 = C
            m3 = A

    else:
        if A>B:
            m1 = C
            m2 = A
            m3 = B

        else:
            m1 = C
            m2 = B
            m3 = A


    if m1>= m2+m3:
        print('NAO FORMA TRIANGULO')
        exit()

    if (m1**2) == ((m2**2) + (m3**2)):
        print('TRIANGULO RETANGULO')

    if (m1**2) > (m2**2) + (m3**2):
        print('TRIANGULO OBTUSANGULO')

    if (m1**2) < (m2**2) + (m3**2):
        print('TRIANGULO ACUTANGULO')

    if m1==m2 and m1==m3 and m3==m2:
        print('TRIANGULO EQUILATERO')

    if (m1==m2 and m1!=m3) or (m1==m3 and m1!=m2) or (m2==m3 and m2!=m1):
        print('TRIANGULO ISOSCELES')
