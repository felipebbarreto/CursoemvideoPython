km = int(input('Digite a distância em km da viagem: '))
if km>200:
    print('O valor da passagem de ônibus é \033[4;36mR${:.2f}'.format(km*0.45))
else:
    print('O valor da passagem de ônibus é \033[4;34mR${:.2f}'.format(km*0.50))
