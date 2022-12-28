preco = float(input('Digite o valor do produto: R$'))
desconto = 5 / 100 * preco
pf = preco - desconto
print('O preço final com desconto de 5% é {:.2f} R$'.format(pf))
