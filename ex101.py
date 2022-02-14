from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade >= 18:
        vot = '\033[32mOBRIGATÓRIO!\033[m'
    if 16 <= idade < 18 or idade >= 65:
        vot = '\033[33mOPCIONAL!\033[m'
    if idade < 16:
        vot = '\033[31mNEGADO!\033[m'
    return vot


# Programa Principal
n = int(input('Ano de nascimento: '))
q = voto(n)
print(f'Com {date.today().year - n} anos: {q}')
