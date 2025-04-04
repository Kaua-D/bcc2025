'''
#com For e While
while True:
    n = input('Digite espaço para parar:')
    if n == ' ':
        break
    m = int(n)

    for i in range(m):
        if i > 1:
            m = m*i

    print(m)
'''
'''
#Com For
n = int(input())
m=n

for i in range(1,n):
    m = m*i

print(m)
'''
'''
#com If
n = int(input())
m=n
while True:
    if n > 1:
        n = n-1
        m = m*(n)
        print(n)
        
    else:
        break
    
print(m)
'''
'''
#com While

n= int(input())
m=n

while n>1:
    n = n-1
    m = m*n

print(m)'''

# def fat
def fat(n):
    if n == 0:
        return 1
    else:
        return n*fat(n-1)

a = fat(0)
print(a)

b= fat(int(input()))
print(b)