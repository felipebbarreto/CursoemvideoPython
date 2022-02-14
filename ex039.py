from datetime import date
n = int(input('Em qual ano você nasceu?: '))
h = date.today().year
if h - n == 18:
    print('\033[32mParabéns!! Está na hora de se alistar para o serviço militar')
elif h - n < 18:
    print('\033[33mCalma jovem!! Ainda não chegou a sua vez. \nFaltam {} anos para você se alistar!\nVocê irá se alistar em {}'.format(18 - ( h - n ), n + 18))
elif h - n > 18:
    print('\033[31mVocê está ATRASADO para o serviço militar!! \nJá se passaram {} anos do ano do seu alistamento\nVocê deveria ter se alistado em {}'.format( ( h - n) - 18, n + 18))
else:
    print('\033[4;41mVocê não inseriu uma data de nascimento válida, tente novamente!!')
