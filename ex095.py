jog = {}
gols = []
lista = []
while True:
    jog.clear()
    gols.clear()
    jog['nome'] = str(input('Nome do jogador: '))
    n = int(input(f'Quantas partidas {jog["nome"]} jogou?: '))
    for p in range(0,n):
        gols.append(int(input(f'Quantos gols na partida {p+1}?: ')))
    jog['gols'] = gols[:]
    jog['total'] = sum(gols)
    lista.append(jog.copy())
    ch = str(input('Deseja continuar? [ S / N ] : ')).strip().upper()[0]
    if ch in 'Nn':
        break
print('-='*50)
print(f'{"No.":<5}{"Nome":<14}{"Gols":<22}{"Total":<5}')
print('-'*50)
for n,x in enumerate(lista):
    print(f'{n:<5}{x["nome"]:<14}{str(x["gols"]):<22}{x["total"]:<5}')
print('-'*50)
while True:
    ch = int(input('Digite qual jogador quer saber os detalhes (999 para encerar): '))
    if ch == 999:
        break
    elif 0 <= ch < len(lista):
        print(f'O {lista[ch]["nome"]} fez:')
        for g,x in enumerate(lista[ch]['gols']):
            print(f'No jogo {g+1} ele fez {x} Gols')
            print('-' * 50)
    else:
        print('\033[31mOpção inválida!\033[m')
