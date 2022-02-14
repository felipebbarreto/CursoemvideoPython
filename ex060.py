from math import factorial
n = int(input('Insira um valor: '))
c = n
f = 1
print('\033[33mCalculando o fatorial {}! = \033[m'.format(c),end='')
while c > 0:
    f *= c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('\033[32m{}'.format(f))
print(factorial(n))