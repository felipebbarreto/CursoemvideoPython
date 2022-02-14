d = float(input('Qual a largura da parede?: '))
h = float(input('Qual a altura da parede?: '))
a = d*h
t = a/2
print('A dimensão da parede é {:.2f}m de largura por {:.2f}m de altura'.format(d,h))
print('A área total da parede é \033[4;32m{:.2f} m²\033[m e você irá precisar de \033[4;32m{:.2f} litros\033[m de tinta por demão \nConsiderando o rendimento de \033[1;34m2 litros de tinta por m² de parede\033[m'.format(a,t), end='\nObrigado')
