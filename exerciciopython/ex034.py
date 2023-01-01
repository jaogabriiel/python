salário = float(input('Informe seu salário: R$ '))
if salário > 1.250:
    aumento = 10 / 100 * salário
    novo_salário = salário + aumento
    print('Seu novo salário será R${}'.format(novo_salário))
else:
    aumento = 15 / 100 * salário
    novo_salário = salário + aumento
    print('Seu novo salário será R${}'.format(novo_salário))
