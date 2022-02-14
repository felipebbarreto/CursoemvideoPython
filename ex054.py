from datetime import date
countma = 0
countme = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da pessoa número {}: '.format(c)))
    if date.today().year - ano < 21:
        countme += 1
    elif date.today().year - ano >= 21:
        countma += 1
print('Das 7 pessoas, {} são maiores de idade e {} tem menos de 21 anos'.format(countma,countme))
