v = float(input('Qual o valor do imóvel?: R$'))
s = float(input('Qual a sua renda mensal?: R$'))
p = int(input('O financiamento será quitado em quantos anos?: '))
m = p * 12
if v / m <= 0.3 * s:
    print('\033[1;32mO seu financiamento foi aprovado!! \nSerão {:.0f} parcelas mensais de R${:.2f}'.format( m , v / m ))
else:
    print('\033[1;31mFinanciamento NEGADO!!!\nRenda insuficiente para financiar este imóvel!')
print('\033[mTenha um bom dia!')
