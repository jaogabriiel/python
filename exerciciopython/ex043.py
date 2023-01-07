peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    situação = 'Abaixo do peso'
elif imc > 18.5 and imc < 25:
    situação = 'Peso ideal'
elif imc >= 25 and imc < 30:
    situação = 'Sobrepeso'
elif imc >= 30 and imc < 40:
    situação = 'Obesidade'
else:
    situação = 'Obesidade mórbida'
print('Seu imc é de {:.2f}. Situação {}'.format(imc, situação))
