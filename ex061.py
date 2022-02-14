n1 = int(input('Digite o primeiro termo da progressão aritimética: '))
r = int(input('Digite a razão dessa P.A.: '))
c = 0
pa = n1
print('{} ->'.format(n1), end='')
while c != 10:
    pa += r
    print('{} ->'.format(pa),end='')
    c += 1
print('FIM')
    