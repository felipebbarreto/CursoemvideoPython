n = int(input('Insira um número: '))
if (n/2)==(n//2):
    print('O número {} é \033[34mpar!'.format(n))
else:
    print('O número {} é \033[33mímpar!'.format(n))
