cond = ''
n1 = s = m = c = ma = me = 0
while cond != 'N':
    n1 = int(input('Digite um valor: '))
    c += 1
    s += n1
    m = s / c
    if c == 1:
        ma = me = n1
    else:
        if n1 > ma:
            ma = n1
        elif n1 <= me:
            me = n1
    cond = str(input('Você deseja inserir mais um valor: [ S / N ]')).strip().upper()[0]
print('A média dos valores digitados é \033[33m{}\033[m'.format(m))
print('O maior valor digitado foi \033[32m{}\033[m e o menor valor digitado foi \033[31m{}\033[m'.format(ma,me))
print('Foram inseridos {} valores'.format(c))
