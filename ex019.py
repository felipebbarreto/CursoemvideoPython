from random import choice
from time import sleep

n1 = input('Digite o nome do aluno 1: ')
n2 = input('Digite o nome do aluno 2: ')
n3 = input('Digite o nome do aluno 3: ')
n4 = input('Digite o nome do aluno 4: ')
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('Sorteando!!!')
sleep(2)
print('O Aluno escolhido para apagar o quadro foi \033[4;31m{}'.format(escolhido))
