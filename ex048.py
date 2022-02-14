print('Soma de todos os números ímpares que são múltiplos de 3 no intervalo de 1 a 500')
s = 0
cont = 0
for c in range(3,501,2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma é {}, num total de {} valores'.format(s, cont))