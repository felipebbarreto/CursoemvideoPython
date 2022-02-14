p = float(input('Qual o seu peso (kg): '))
h = float(input('Qual a sua altura (m)?: '))
imc = p / (h ** 2)
if imc < 18.5:
    print('\033[33mVocê está abaixo do peso!\nSeu IMC = {:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('\033[32mVocê está no peso ideal\nSeu IMC = {:.1f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('\033[33mVocê está com sobrepeso\nSeu IMC = {:.1f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('\033[31mVocê está obeso\nSeu IMC = {:.1f}\nProcure um exercício físico!'.format(imc))
elif imc >= 40:
    print('\033[1;41mVocê está com obesidade mórbida\nSeu IMC = {:.1f}\nPROCURE UM MÉDICO\033[m'.format(imc))
else:
    print('Você não informou dados válidos, tente novamente!')
