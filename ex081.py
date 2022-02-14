lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        ch = str(input('Deseja outro? [ S / N ]: ')).strip().upper()[0]
        if ch in 'SN':
            break
        else:
            print('\033[31mOpção inválida, tente novamente!\033[m')
    if ch == 'N':
        break
print('-='*30)
print(f'Foram digitados {len(lista)} números.')
print('(em ordem decrescente)')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 está entre os números digitados.')
else:
    print('O número 5 não está entre os números digitados.')
