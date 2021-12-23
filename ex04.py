import math
po = float(input('Comprimento do cateto oposto:'))
bo = float(input('comprimento do cateto adjacente:'))
hi = math.hypot(po,bo)
print('A hipotenusa vai medir {:.2f}'.format(hi))
