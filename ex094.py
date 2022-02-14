pes = {}
lista = []
s = t = 0
while True:
    pes.clear()
    pes['nome'] = str(input('Nome: '))
    while True:
        pes['sex'] = str(input('Sexo [ M / F ]: ')).strip().upper()[0]
        if pes['sex'] in 'MF':
            break
        print('\033[31m Erro! Digite [ M / F ]: \033[m')
    pes['idade'] = float(input('Idade: '))
    lista.append(pes.copy())
    s += pes['idade']
    ch = str(input('Deseja continuar? [ S / N ]: ')).strip().upper()[0]
    if ch in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
media = s / len(lista)
print(f'A média de idade do grupo é {media:.1f} anos.')
print('As mulheres do grupo são: ', end='')
for m in lista:
    if m['sex'] in 'Ff':
        print(f'{m["nome"]}, ', end='')
print()
print('As pessoas que estão acima da média de idade são: ', end='')
for p in lista:
    if p['idade'] >= media:
        print(p['nome'], end=' ')
    print()
print('<< ENCERRADO >>')
