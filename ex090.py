aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Qual a média de {aluno["Nome"]}: '))
print(f'O nome é {aluno["Nome"]}.')
print(f'A média é igual a {aluno["Média"]}.')
if aluno["Média"] >= 7:
    print('\033[32mAPROVADO!!!')
if aluno["Média"] < 7:
    print('\033[31mREPROVADO!!!')
