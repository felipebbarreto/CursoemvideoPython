n = int(input('Insira um valor: '))
c = n
f = 1
for c in range(1,c+1):
    f = f * n
    n += - 1
    print('{} x {}'.format(f,n))
print('{}! = {}'.format(c,f))