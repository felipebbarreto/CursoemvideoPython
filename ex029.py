v = float(input('Qual a sua velocidade? (km/h): '))
if v>80:
    m = (v-80)*7
    print('\033[1;31mMULTADO!!!, o limite de velocidade é 80 km/h.\nVocê estava a {} km/h\nO Valor da multa é R${:.2f}'.format(v,m))
else:
    print('\033[1;32mParabéns, você está dentro do limite de velocidade')
print('Tenha um bom dia, dirija com segurança')
