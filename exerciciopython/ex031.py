dis = int(input('Quantos Km você viajou? '))
if dis <= 200:
    preço = 0.50 * dis
    print('O custo final da sua viagem é R${}'.format(preço))
else:
    preço = 0.45 * dis
    print('O preço final da sua viagem é R${}'.format(preço))
