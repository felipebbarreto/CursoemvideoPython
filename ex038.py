n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: \033[32m'))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('\033[33mOs valores são iguais!!!')
