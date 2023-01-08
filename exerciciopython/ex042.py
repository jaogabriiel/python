a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        triangulo = 'EQUILÁTERO'
    elif a != b != c != a:
        triangulo = 'ESCALENO'
    else:
        triangulo = 'ISÓSCELES'
    print('Com esses segmentos podemos formar um triângulo {}'.format(triangulo))
else:
    print('Não é possível formar um triângulo com os segmentos informados')
