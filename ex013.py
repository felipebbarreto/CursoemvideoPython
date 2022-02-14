s = float(input('Qual o valor do salário?: R$'))
n = s*1.15
print('O novo salário, com 15% de aumento, é \033[1;32mR${:.2f}\033[m'.format(n), end='\nObrigado')
