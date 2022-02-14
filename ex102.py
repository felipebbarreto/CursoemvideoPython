def fatorial(n,show=True):
    """"
    -> Calcula o fatorial de um número
    :n: O número a ser calculado
    :show: (Opcional) se deseja ou não que imprima os argumentos da conta
    :return: O valor do fatorial do numero n.
    """

    f = 1
    for c in range(0,n):
        f *= (n-c)
        if show:
            print(f'{n-c} ',end='')
            if n-c > 1:
                print('x ',end='')
            else:
                print('= ',end='')
    print(f)

fatorial(5,show=True)