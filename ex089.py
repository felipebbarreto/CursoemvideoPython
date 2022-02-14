ficha = list()
while True:
    n = (str(input('Digite o nome: ')))
    n1 = (float(input('Digite a nota da primeira prova: ')))
    n2 = (float(input('Digite a nota da segunda prova: ')))
    media = (n1+n2)/2
    ficha.append([n,[n1,n2],media])
    resp = str(input('Deseja inserir mais um aluno [ S / N ]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-='*15)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":>8}')
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<12}{a[2]:>8.1f}')
print('-='*15)
while True:
    d = int(input('Deseja ver as notas separadas de qual aluno?\nDigite o número de chamada ou (999 para encerrar): '))
    if d == 999:
        print('-=' * 15)
        print('Finalizando!!')
        break
    if d <= len(ficha) - 1:
        print(f'As notas do aluno {ficha[d][0]} são {ficha[d][1]}')
        print('-=' * 15)
print('Obrigado!')
