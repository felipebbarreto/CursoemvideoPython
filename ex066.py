cont = s = 0
while True:
    n = int(input('Insira número: [999 para encerrar] '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você inseriu {cont} valores e a soma entre eles é {s}')
