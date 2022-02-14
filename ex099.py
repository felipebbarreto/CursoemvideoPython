from time import sleep
from random import randint

def maior(*num):
    print('-='*50)
    print('Analisando os valores passados!')
    sleep(2.5)
    ma = 0
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
        if c > ma:
            ma = c
    print(f' => Foram informados {len(num)} valores ao todo!')
    print(f'O maior valor informado foi {ma}')


# Programa principal
maior(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
maior(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
maior(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
maior(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
