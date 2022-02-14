ch = cm = ci = 0
while True:
    print('\033[33m-=-\033[m'*15)
    idade = int(input('Digite a idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Digite o sexo [ M / F ]: ')).strip().upper()[0]
    if idade > 18:
        ci += 1
    if sex == 'M':
        ch += 1
    if sex == 'F' and idade < 20:
        cm += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Você deseja cadastrar outra pessoa: [ S / N ] ')).strip().upper()[0]
    if op == 'N':
        print('\033[33m-=-\033[m' * 15)
        break
print(f'Você cadastrou {ci} pessoas com mais de 18 anos')
print(f'Foram cadastrados {ch} Homens')
print(f'Foram cadastradas {cm} mulheres com menos de 18 anos')
