lista = list()
maior = list()
menor = list()
for cont in range(1, 6):
    lista.append(int(input('Digite um número: ')))
print('-='*30)
print(f'Você inseriu os números:\n{lista}')
orglist = lista[:]
orglist.sort(reverse=True)
ma = orglist[0]
orglist.sort()
me = orglist[0]
for c,v in enumerate(lista):
    if v == ma:
        maior.append((c+1))
    if v == me:
        menor.append((c+1))
print(f'O maior valor foi {ma} e foi digitado nas posições ',end='')
for pma in maior:
    print(f'{pma}...',end='')
print(f'\nO menor valor foi {me} e foi digitado nas posições ',end='')
for pme in menor:
    print(f'{pme}...',end='')
