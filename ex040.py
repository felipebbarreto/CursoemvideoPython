n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite o valor da segunda prova: '))
n3 = float(input('Digite o valor da terceira prova: '))
print('Você tirou \n{} na primeira prova\n{} na segunda prova\n{} na terceira prova.'.format(n1,n2,n3))
m = ( n1 + n2 + n3 ) / 3
if m >= 7:
    print('\033[1;32mPARABÉNS!!! Você foi aprovado!!\nSua média foi {:.1f}\nBoas Férias!!'.format(m))
elif m >= 5 and m < 7:
    print('\033[33mVocê está de RECUPERAÇÃO!!!\nSua média foi {:.1f}\nVai estudar para as provas de recuperação!!'.format(m))
elif m >= 0 and m < 5:
    print('\033[4;31mVOCÊ ESTÁ REPROVADO!!!!\nSua média foi {:.1f}!! Insuficiente para a progressão de ano\nEstude mais ano que vem!'.format(m))
else:
    print('\033[1;41mErro! Você não inseriu notas válidas\033[m')
