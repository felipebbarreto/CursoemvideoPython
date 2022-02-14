from random import shuffle
from time import sleep

a = input('Digite o nome de um aluno: ')
b = input('Digite o nome de um aluno: ')
c = input('Digite o nome de um aluno: ')
d = input('Digite o nome de um aluno: ')
lista = [a, b, c, d]
shuffle(lista)
print('Sorteando..')
sleep(2)
print('A ordem de apresentação é\033[4;32m')
print(lista)
