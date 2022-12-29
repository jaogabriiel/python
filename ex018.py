from math import sin, cos, tan, radians
ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo {} tem o seno de {:.2f}'.format(ângulo, seno))
print('O ângulo {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
print('O ângulo {} tem a tangente de {:.2f}'.format(ângulo, tangente))
