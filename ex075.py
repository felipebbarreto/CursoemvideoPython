tupla = (int(input('Insira um valor: ')), int(input('Insira um valor: ')),
         int(input('Insira um valor: ')), int(input('Insira um valor: ')), )
print('Você inseriu:\n', tupla)
print(f'O número 9 foi inserido {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 foi inserido na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado!')
print('São pares os números: ')
for c in tupla:
    if c % 2 == 0:
        print(c, end = ' ')
