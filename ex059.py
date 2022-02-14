c = 0
n1 = float(input('Insira um valor: '))
n2 = float(input('Insira outro valor: '))
while c != 5:
    c = int(input('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior valor
    [ 4 ] Inserir novos números
    [ 5 ] Sair
    Digite o número da operação desejada: '''))
    if c == 1:
        print('A soma de {} e {} = {}'.format(n1, n2, n1 + n2))
        print('Deseja fazer outra operação? ')
    elif c == 2:
        print('A multiplicação de {} e {} = {}'.format(n1, n2, n1 * n2))
        print('Deseja fazer outra operação? ')
    elif c == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
            print('Deseja fazer outra operação? ')
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
            print('Deseja fazer outra operação? ')
        elif n1 == n2:
            print('{} é igual a {}'.format(n1, n2))
            print('Deseja fazer outra operação? ')
    elif c ==4:
        n1 = float(input('Insira um valor: '))
        n2 = float(input('Insira outro valor: '))
    elif c == 5:
        print('Finalizando.. Obrigado, até a próxima!')
    else:
        print('Você não inseriu uma opção válida! Tente novamente')
