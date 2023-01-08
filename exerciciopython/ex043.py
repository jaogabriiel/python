peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    situação = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    situação = 'Peso ideal'
elif 25 <= imc < 30:
    situação = 'Sobrepeso'
elif 30 <= imc < 40:
    situação = 'Obesidade'
else:
    situação = 'Obesidade mórbida'
print('Seu imc é de {:.1f}. Situação: {}'.format(imc, situação))
