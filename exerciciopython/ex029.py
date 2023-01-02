vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você ultrapassou a velocidade limite de 80Km/h você receberá uma multa de R${:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade limite! Dirija com cuidado!')
