print('\033[33m-=-\033[m'*30)
print('Converta um número decimal para \n 1 - Binário\n 2 - Octal\n 3 - Hexadecimal')
print('\033[33m-=-\033[m'*30)
n = int(input('Digite um número inteiro'))
x = int(input('Insira a base de conversão'))
if x == 1:
    print('{} convertido para binário é igual a {}'.format(n,bin(n)[2:]))
elif x == 2:
    print('{} convertido para octal é igual a {}'.format(n,oct(n)[2:]))
elif x == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Reinicie o programa e insira uma base válida!')
