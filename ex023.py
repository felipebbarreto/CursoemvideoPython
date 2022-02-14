n = input('Digite um número inteiro de 0 a 9999: ')
print('\033[1;36mUnidade: {}'.format(n[3]))
print('\033[1;35mDezena: {}'.format(n[2]))
print('\033[1;34mCentena: {} \n\033[1;33mMilhar: {}'.format(n[1],n[0]))

nm = int(input('Reinsira o número acima: '))
print('\033[mUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format((nm%10),(nm%100//10),(nm%1000//100),nm//1000))
