salário = float(input('Informe seu salário: R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Seu novo salário será R${}'.format(novo))
