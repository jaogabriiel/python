a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        triangulo = 'equilátero'
    elif a == b or a == c or b == c:
        triangulo = 'isósceles'
    elif a != b and a != c and b != c:
        triangulo = 'escaleno'
    print('Com esses segmentos podemos formar um triângulo {}'.format(triangulo))
else:
    print('Não é possível formar um triângulo com os segmentos informados')
