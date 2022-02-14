import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.sqrt( math.pow(co, 2) + math.pow(ca, 2))
hi = math.hypot(co,ca)
print('A o valor da \033[1mhipotenusa é {:.2f} {:.2f}'.format(h,hi))
