from time import sleep
from random import randint
lista = []


def sorteia(n):
    lista.clear()
    for c in range(0, n):
        x = randint(0,100)
        sleep(0.5)
        print(x, end=' ')
        lista.append(x)
def somaPar(lista):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'A soma dos números pares sorteados é {s}')


# Programa Principal
n = int(input('Digite a quantidade de números a serem sorteados: '))
sorteia(n)
somaPar(lista)
