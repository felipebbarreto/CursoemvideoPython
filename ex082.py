lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        ch = str(input('Deseja continuar [ S / N ]: ')).strip().upper()[0]
        if ch in 'SN':
            break
        else:
            print('\033[31mOpção inválida\033[m')
    if ch == 'N':
        break
for c in lista:
    if c%2 == 0:
        pares.append(c)
    elif c%2 == 1:
        impares.append(c)
print('-='*25)
print('Os números digitados foram: ')
print(lista)
print('Sendo que os números pares foram:')
print(pares)
print('E os ímpares foram: ')
print(impares)
