d = int(input('Quantos dias você deseja alugar o carro?: '))
km = int(input('Quantos km você pretende andar?: '))
pd = d * 60
pkm = km * 0.15
p = pd + pkm
print('O valor da diária é R$60,00, para {:.2f} dias = \033[4;32mR${:.2f}\033[m'.format(d,pd))
print('O valor do km rodado é R$0.15, para a estimativa de {} km fica em torno de \033[4;32mR${:.2f}\033[m'.format(km,pkm))
print('-'*100)
print('O valor total do aluguel é \033[7;40mR${:.2f}\033[m'.format(p), end='\nObrigado')
