lado1 = float(input('Quanto mede o primeiro lado do triângulo? '))
lado2 = float(input('Quanto mede o segundo lado? '))
lado3 = float(input('Quanto mede o terceiro lado? '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Não é possível formar um triângulo com esses três segmentos')
