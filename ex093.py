jog = {}
gols = []
jog['nome'] = str(input('Nome do jogador: '))
n = int(input(f'Quantas partidas {jog["nome"]} jogou?: '))
for p in range(0,n):
    gols.append(int(input(f'Quantos gols na partida {p+1}?: ')))
jog['gols'] = gols[:]
jog['total'] = sum(gols)
print('-='*50)
print(jog)
print('-='*50)
for k, v in jog.items():
    print(f'{k} = {v}')
print('-='*50)
print(f'O jogador {jog["nome"]} atuou em {n} partidas.')
for j,n in enumerate(jog['gols']):
    print(f'    => Na partida {j+1}, fez {n}')
print(f'Foi um total de {jog["total"]}')
