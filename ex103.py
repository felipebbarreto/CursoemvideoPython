def ficha(nome,gols):
    if nome=='':
        nome = '<desconhecido>'
    if gols=='':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols')


# Programa Principal
n = str(input('Digite o nome do jogador: '))
g = str(input('Quantos gols ele fez?: '))
ficha(n,g)
