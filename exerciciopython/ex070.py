total = mais1000 = menor = cont = 0
barato = ' '
while True:
    print('-'*10, 'Lojas John', '-'*10)
    nome = str(input('Produto: '))
    preço = float(input('Digite o preço do produto: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        mais1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opção in 'N':
        break
print('-'*25)
print(f'O preço total das compras é R${total:.2f}')
print(f'{mais1000} produtos custam acima de R$1000')
print(f'o produto mais barato é {barato} custando R${menor:.2f}')
