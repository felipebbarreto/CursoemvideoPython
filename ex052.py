n = int(input('Insira um número inteiro: '))
if n % 2 == 1 or n % 3 == 1 or n == 2 or n == 3:
    print('{} é um número primo'.format(n))
else:
    print('{} não é um número primo'.format(n))
