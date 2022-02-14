p = float(input('Qual o preço do produto?: '))
x = p*0.95
print('Na liquidação, com 5% de desconto, o preço desse item é \033[4;32mR${:.2f}\033[m'.format(x), end='\nObrigado')
