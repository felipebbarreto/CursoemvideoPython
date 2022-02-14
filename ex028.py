from random import randint
from time import sleep
n = randint(1,10)
print('\033[1;33m-=-'*25)
print('\033[mVou pensar em um número de 1 a 10, duvido que você consegue adivinhar')
print('\033[1;33m-=-'*25)
np = int(input('\033[mEm qual número eu pensei: (entre 1 e 10) '))
print('\033[30mProcessando...\033[m')
sleep(2)
if n==np:
    print('\033[32mParabéns! Você acertou!! Conseguiu adivinhar')
else:
    print('\033[31mErroooooou!! Eu pensei no número {} e você escolheu {}. Boa sorte da próxima vez!'.format(n,np))
