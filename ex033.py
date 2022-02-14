from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
n3 = float(input('Digite mais um número: '))
print('Você digitou {}, {} e {}'.format(n1, n2, n3))
print('Processando...\033[32m')
sleep(1)
if n1 > n2 and n1 > n3:
    print('O maior número foi {}'.format(n1))
else:
    if n2 > n3 and n2 > n1:
        print('O maior número foi o {}'.format(n2))
    else:
        print('O maior valor foi o {}'.format(n3))
print('\033[me\033[31m')
if n1 < n2 and n1 < n3:
    print('O menor número foi {}'.format(n1))
else:
    if n2 < n3 and n2 < n1:
        print('O menor número foi o {}'.format(n2))
    else:
        print('O menor valor foi o {}'.format(n3))
