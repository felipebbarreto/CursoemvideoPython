from datetime import date
n = int(input('Insira o valor do ano: '))
if n == 0:
    n = date.today().year
if n / 4 == n // 4 and n % 100 != 0 or n % 400 == 0:
    print('\033[32mO ano {} é bissexto'.format(n))
else:
    print('\033[31mO ano {} não é bissexto'.format(n))
