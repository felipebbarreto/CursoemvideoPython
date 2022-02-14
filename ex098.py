from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if fim > inicio:
        num = ((fim - inicio) // passo) + 1
        s = inicio
        for n in range(0, num):
            print(f'{s}, ', end='')
            s += passo
            sleep(0.5)
        print()
        print('-=' * num * 2)
    if inicio > fim:
        num = ((inicio - fim) // passo) + 1
        s = inicio
        for n in range(0, num):
            print(f'{s}, ', end='')
            s -= passo
            sleep(0.5)
        print()
        print('-=' * num * 2)


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez')
i = int(input('Qual o início da contagem?: '))
f = int(input('Qual o final da contagem?: '))
p = int(input('Qual o passo da contagem?: '))
contador(i, f, p)
