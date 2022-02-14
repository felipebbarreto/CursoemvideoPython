'''print('-=-'*10)
print('Caixa Eletrônico')
print('-=-'*10)
n = int(input('Qual o valor sacado: R$'))
ct = v = d = c = u = 0
ct = n // 50
v = (n % 50) // 20
d = (n % 50) % 20 // 10
c = n % 50 % 20 % 10 // 5
u = n % 50 % 20 % 10 % 5 // 1
print(f'{ct} notas de R$50,00\n{v} notas R$20,00\n{d} notas R$10,00')
print(f'{c} notas R$5,00\n{u} notas R$1,00')'''


print('-=-'*10)
print('Caixa Eletrônico')
print('-=-'*10)
v = int(input('Qual o valor sacado: R$'))
tot = v
ced = 50
totced = 0
print('Você sacou um total de:')
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} notas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if tot == 0:
            break
print('-=-'*10)
print('Volte sempre, tenha um bom dia!!')
