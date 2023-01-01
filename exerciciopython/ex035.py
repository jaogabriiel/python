lado1 = float(input('Quanto mede o primeiro lado do triângulo? '))
lado2 = float(input('Quanto mede o segundo lado? '))
lado3 = float(input('Quanto mede o terceiro lado? '))
if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
    print('É possível formar um triândulo com essas três medidas')
else:
    print('Não é possível formar um triângulo com essas três medidas')
