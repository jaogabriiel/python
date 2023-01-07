preço = float(input('Digite o preço do produto: R$'))
pagamento = int(input('Digite 0 para pagamento à vista, 1 para à vista no cartão, 2 para pagar em 2x no cartão e 3 para pagar em 3x ou mais no cartão: '))
if pagamento == 0:
    desconto = preço * 10 / 100
    preço = preço - desconto
elif pagamento == 1:
    preço = preço - (preço * 5 / 100)
elif pagamento == 2:
    preço = preço
elif pagamento == 3:
    preço = preço + (preço * 20 / 100)
    
if pagamento == 0:
    forma = 'À vista'
elif pagamento == 1:
    forma = 'À vista no cartão'
elif pagamento == 2:
    forma = '2x no cartão'
else:
    forma = '3x ou mais no cartão'
print('Você escolheu a forma de pagamento {}.O total a ser pago pelo produto é {}'.format(forma, preço))
