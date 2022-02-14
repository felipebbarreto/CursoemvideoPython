p = float(input('Qual o valor do produto?: R$'))
print('Condição de pagamento:\n1 - À vista (dinheiro ou Cheque) = 10% de desconto')
print('2 - À vista no cartão (crédito ou débito) = 5% de desconto')
print('3 - Em até 2x no cartão')
print('4 - Em 3x ou mais no cartão = + 20% juros')
c = int(input('Qual a condição de pagamento?: '))
if c == 1:
    print('O total da compra é de R${:.2f}'.format(p * 0.9))
elif c == 2:
    print('O total da compra é de R${:.2f}'.format(p * 0.95))
elif c == 3:
    print('O total da compra é de R${:.2f}, parcelado em 2x de R${:.2f}'.format(p, p / 2))
elif c == 4:
    x = float(input('Insira o número de parcelas: '))
    pj = p * 1.2
    print('O total da compra é de R${:.2f}, parcelado em {:.0f}x de R${:.2f}'.format(pj, x, pj / x))
else:
    print('\033[41mVocê não inseriu uma condição de pagamento válida, tente novamente..\033[m')
