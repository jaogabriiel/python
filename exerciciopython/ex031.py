dis = float(input('Quantos Km você vai viajar? '))
'''if dis <= 200:
    preço = 0.50 * dis
else:
    preço = 0.45 * dis'''
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print('O custo final da sua viagem é R${:.2f}'.format(preço))
