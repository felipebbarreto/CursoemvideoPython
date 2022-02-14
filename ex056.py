x = 0
m = 0
id = 0
ma = 0
nomev = 'a'
xm = 0
for c in range(1,5):
    nome = str(input('Digite seu nome: ')).strip()
    sex = str(input('Qual o seu sexo ( m / f )?: ')).strip().lower()
    idade = int(input('Qual a sua idade: '))
    id += idade
    x += 1
    if sex == 'm':
        if idade >= ma:
            ma = idade
            nomev = nome
    elif sex == 'f':
        if idade < 20:
            xm = xm + 1
print('A média de idade do grupo é {:.1f}'.format(id / x))
print('O homem mais velho do grupo é {} e tem {} anos'.format(nomev,ma))
print('O grupo tem {} mulher(es) com menos de 20 anos'.format(xm))
