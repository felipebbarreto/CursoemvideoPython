frase = str(input('Digite uma frase: ')).strip()
fm = frase.upper()
print('A letra A aparece \033[1;32m{}\033[m vezes nessa frase'.format(fm.count('A')))
print('A letra A aparece a primeira vez na posição \033[1;34m', fm.find('A')+1)
print('\033[mA letra A aparece a última vez na posição \033[1;33m', fm.rfind('A')+1)