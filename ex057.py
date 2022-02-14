s = 0
sex = str(input('Qual o seu sexo?: [ M / F ] ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Dados inválidos. Qual o seu sexo?: [ M / F ] ')).strip().upper()[0]
print('Registrado com sucesso!')
