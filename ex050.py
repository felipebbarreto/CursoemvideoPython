print('Insira 6 números inteiros')
s = 0
p = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        p += 1
print('A soma dos {} números pares inseridos é \033[32m{}'.format(p,s))
