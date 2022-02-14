tupla = (
'Pão', 2.00, 'Pão de queijo', 4.25, 'Pão de queijo com linguiça', 11.00, 'Pastel', 3.20, 'Empada', 4.5, 'Torta', 6.25,
'Café', 0.75, 'Café pingado', 1.5, 'Chocolate quente', 1.8, 'Coca Cola', 2.5)
print('-' * 50)
print(f'\033[1;36m{"Lista de preços":^50}\033[m')
print('-' * 50)
for c in range(1, 21, 2):
    print(f'{tupla[c - 1]:.<40} R$ {tupla[c]: >5.2f}')
print('-' * 50)
