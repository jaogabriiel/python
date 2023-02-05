preço = float(input('Digite o preço do produto: R$'))
pagamento = int(input('''
FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Digite sua opção: '''))

if pagamento == 1:
    total = preço - (preço * 10 / 100)
elif pagamento == 2:
    total = preço - (preço * 5 / 100)
elif pagamento == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif pagamento == 4:
    total = preço + (preço * 20 / 100)
    par = int(input('Quantas parcelas? '))
    parcela = total / par
    print('Sua compra será parcelada em {}x de {:.2F} COM JUROS'.format(par, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
