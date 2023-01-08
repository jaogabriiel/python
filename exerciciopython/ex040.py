nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
if média < 5.0:
    situação = 'Reprovado!'
elif média > 7.0:
    situação = 'Aprovado! Parabéns!'
else:
    situação = 'Recuperação!'
print('Sua média é {}. {}'.format(média, situação))
