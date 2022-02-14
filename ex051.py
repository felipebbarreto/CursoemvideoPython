n1 = int(input('Digite o primeiro termo da progressão aritimética: '))
r = int(input('Digite a razão dessa P.A.: '))
for c in range(n1,n1+(10*r),r):
    print(c, '-> ', end = "")
