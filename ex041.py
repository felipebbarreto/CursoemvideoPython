from datetime import date
n = int(input('Digite o ano de nascimento: '))
h = date.today().year
i = h - n
if i > 25:
    print('Você está na categoria MASTER!\nCom {} anos.'.format(i))
elif 19 < i <= 25:
    print('Você está na categoria SÊNIOR!\nCom {} anos.'.format(i))
elif i <= 19 and i > 14:
    print('Você está na categoria JÚNIOR!\nCom {} anos.'.format(i))
elif i <= 14 and i > 9:
    print('Você está na categoria INFANTIL!\nCom {} anos.'.format(i))
elif i <= 9 and i >= 0:
    print('Você está na categoria MIRIM!\nCom {} anos.'.format(i))
else:
    print('Você não inseriu uma data válida, tente novamente!')
