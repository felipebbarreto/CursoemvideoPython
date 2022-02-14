lista = list()
temp = list()
pesados = list()
leves = list()
pma = pme = 0
while True:
    temp.append(str(input('Digite o NOME: ')))
    temp.append(int(input('Digite o peso (kg): ')))
    lista.append(temp[:])
    if len(lista) == 1:
        pma = pme = temp[1]
    if temp[1] >= pma:
        pma = temp[1]
    if temp[1] <= pme:
        pme = temp[1]
    temp.clear()
    ch = str(input('Deseja inserir outra pessoa [ S / N ] : ')).strip().upper()[0]
    if ch in 'Nn':
        break
for c in lista:
    if c[1] == pma:
        pesados.append(c[:])
    if c[1] == pme:
        leves.append(c[:])
print(f'Foram inseridos os dados de {len(lista)} pessoas.')
print(f'As pessoas com o maior peso de {pma} kg foram\n{pesados[0]}')
print(f'As pessoas com o menor peso de {pme} kg foram\n{leves[0]}')
