r1 = float(input('Insira o comprimento de uma reta: '))
r2 = float(input('Insira o comprimento de mais uma reta: '))
r3 = float(input('Insira o comprimento outra reta: '))
print('Você inseriu o comprimentos das retas {:.0f}, {:.0f} e {:.0f}'.format(r1,r2,r3))
if ((r2-r3<r1)and(r1<r2+r3)) and ((r1-r3<r2) and r2<r1+r3) and (r1-r2<r3 and r3<r1+r2):
    print('\033[32mEsse conjunto de retas formam um triângulo!')
else:
    print('\033[31mEsse conjunto de retas não formam um triângulo')
