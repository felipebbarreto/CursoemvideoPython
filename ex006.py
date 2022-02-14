n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('\033[4;36mO dobro desse valor é {} \n\033[4;35mO triplo desse valor é {} \n\033[4;33mE a raiz quadrada é {:.3f}'.format(d,t,r), end='\n\033[1;33;44mObrigado')