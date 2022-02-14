n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digita a nota da segunda prova: '))
n3 = float(input('Digite a nota da terceira prova: '))
m = (n1+n2+n3)/3
print('A sua média final das provas é \033[1;42m{:.1f}\033[m'.format(m))
