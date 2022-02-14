lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('\033[31mEsse número já foi adicionado anteriormente!\033[m')
    else:
        lista.append(n)
        print('\033[32mNúmero adicionado com sucesso!\033[m')
    while True:
        op = str(input('Deseja inserir outro valor [ S / N ]: ')).strip().upper()[0]
        if op in 'SN':
            break
        else:
            print('\033[31mNão digitou uma opção válida. Tente novamente!\033[m')
    if op == 'N':
        break
print('-='*30)
lista.sort()
print('Você digitou os números (em ordem crescente) :', end='')
for c in lista:
    print(f'{c} ... ', end='')
