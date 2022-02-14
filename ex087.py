s = s3c = mv = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
        if c == 2:
            s3c += matriz[l][c]
        if l == 1 and matriz[l][c] > mv:
            mv = matriz[l][c]
print('-=' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-=' * 25)
print(f'A soma de todos os valores pares digitados foi {s}')
print(f'A soma dos valores da terceira coluna foi {s3c}')
print(f'O maior valor da segunda linha foi {mv}')
