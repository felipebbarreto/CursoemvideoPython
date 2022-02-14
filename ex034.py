n = float(input('Qual o valor do salário do Funcionário?: R$\033[32m'))
if n>1250:
    n1 = n*1.1
    print('O funcionário terá o aumento de R${:.2f}, o seu novo salário será R${:.2f}'.format(n1-n,n1))
else:
    n2 = n*1.15
    print('O funcionário terá o aumento de R${:.2f}, o seu novo salário será R${:.2f}'.format(n2 - n, n2))
