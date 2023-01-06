nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
média = (nota1 + nota2 + nota3 + nota4) / 4
if média < 5.0:
    Situação = 'Reprovado!'
elif média > 7.0:
    Situação = 'Aprovado! Parabéns!'
else:
    Situação = 'Recuperação!'
print('Sua média é {}, {}'.format(média, Situação))
