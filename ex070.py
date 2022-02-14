s = mb = c = cm = 0
nb = op = ' '
print('Loja Baratão')
print('-='*10)
while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço do produto: R$'))
    c += 1
    s += p
    if c == 1:
        mb = p
    if mb > p:
        mb = p
        nb = n
    if p >= 1000:
        cm += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Você deseja continuar: [ S / N }')).strip().upper()[0]
        print('-=' * 10)
    if op == 'N':
        break
print(f'O total gasto na compra foi de R${s:.2f}')
print(f'{cm} produtos custaram mais de R$1000,00')
print(f'O produto mais barato foi {nb} e custou {mb}')
