import math
an = float(input('Digite um ângulo: '))
r = an * 0.0174533
rad = math.radians(an)
print('\033[1;34mO valor do seno de {}o é {:.3f}'.format(an, math.sin(r)))
print('\033[1;35mO valor do cosseno de {}o é {:.3f}'.format(an, math.cos(r)))
print('\033[1;36mO valor da tangente de {}o é {:.3f}\033[m'.format(an, math.tan(r)))

print('{:.6f} {:.6f}'.format(r,rad))
