n = c = s = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    c += 1
    s += n
print('Você digitou {} valores e a soma entre eles é {}.'.format(c-1,s-999))
