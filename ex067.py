cont = n = 0
while True:
    cont = 0
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{n} x {cont:2} = {n*cont}')
print('Programa encerrado!')
