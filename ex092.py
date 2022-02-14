from datetime import date
trab = {}
trab['nome'] = str(input('Nome: '))
n = int(input('Ano de nascimento: '))
trab['idade'] = date.today().year - n
c = int(input('Carteira de trabalho (0 não tem): '))
trab['ctps'] = c
if c != 0:
    trab['contrataçao'] = int(input('Ano de contratação: '))
    trab['salario'] = float(input('Salário: '))
    trab['aposentadoria'] = (35 - (date.today().year - trab['contrataçao'])) + trab['idade']
print('-='*50)
print(trab)
for k , v in trab.items():
    print(f' {k} = {v}')
