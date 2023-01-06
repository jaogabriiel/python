número1 = int(input('Digite um número: '))
número2 = int(input('Digite outro número: '))
if número1 > número2:
    maior = 'primeiro'
    print('O {} valor é o maior'.format(maior))
elif número2 > número1:
    maior = 'segundo'
    print('O {} valor é o maior'.format(maior))
else:
    print('Não existe maior, os dois são iguais')
