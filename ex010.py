n = float(input('Quantos reais você tem?: R$'))
cd = 5.26
d = n/cd
ce = 6.18
e = n/ce
print('Hoje você pode comprar \033[1;32mU$D{:.2f}\033[m \nA cotação do dia é U$D1,00 = R${:.2f}'.format(d,cd))
print('Hoje você pode comprar \033[1;32m${:.2f}\033[m \nA cotação do dia é $1,00 = R${:.2f}'.format(e,ce),end='\nObrigado')