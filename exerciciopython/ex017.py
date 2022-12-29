'''from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjascente: '))
hipotenusa = sqrt(pow(co, 2) + pow(ca, 2))
print('A hipotenusa vale: {:.1f}'.format(hipotenusa))'''

from  math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
