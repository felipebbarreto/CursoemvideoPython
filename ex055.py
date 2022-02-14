ma = 0
me = 10000
for c in range(1,6):
    p = int(input('Digite o peso do paciente (kg): '))
    if p >= ma:
        ma = p
    elif p <= me:
        me = p
print('O paciente mais pesado tem {} kg e o mais leve tem {} kg'.format(ma,me))
