tabela = (
'Coritiba', 'Goiás', 'CRB', 'Botafogo', 'Sampaio Corrêa', 'Náutico', 'Guarani', 'Avaí', 'Operário', 'Vasco', 'CSA',
'Remo', 'Brusque', 'Cruzeiro', 'Ponte Preta', 'Vila Nova', 'Londrina', 'Vitória', 'Brasil de Pelotas', 'Confiança')
print('-=' * 40)
print(tabela)
print('-=' * 40)
for p in range(0, 5):
    print(f'{p + 1} - {tabela[p]}', end=' | ')
print('\n')
print('-=' * 40)
for u in range(16,20):
    print(f'{u+1} - {tabela[u]}', end=' | ')
print('\n')
print('-=' * 40)
print(sorted(tabela), end = ' | ')
print('\n')
print('-=' * 40)
print(tabela.index('Cruzeiro')+1, end = ' - Cruzeiro')
