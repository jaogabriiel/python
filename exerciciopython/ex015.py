dias = int (input('Quantos você ficou com o carro? '))
km = float(input('Quantos km você andou? '))
aluguel = (60 * dias) + (0.15 * km)

print('O total a pagar é: {:.2f}R$'.format(aluguel))
