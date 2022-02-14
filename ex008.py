d = float(input('Digite uma distância em metros: '))
c = d*100
m = d*1000
print('Essa distância é \033[4;36m{} centímetros\033[m e \033[4;35m{} milímetros'.format(c,m), end='\n\033[mObrigado')
