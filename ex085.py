lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]} e os impares são {lista[1]}')
