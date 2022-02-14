frase = str(input('Digite uma frase: ')).strip().upper()
pv = frase.split()
ju = ''.join(pv)
inv = ''
for letra in range(len(ju)-1,-1,-1):
    inv += ju[letra]
if inv == ju:
    print('\033[32mEssa frase é um palíndromo')
else:
    print('\033[31mEssa palavra não é um palíndromo')
