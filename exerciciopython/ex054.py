maior = 0
menor = 0
for c in range(1, 7):
    idade = int(input('Digite a {}° idade: '.format(c)))
    if idade > 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoas já atingiram a maior idade'.format(maior))
print('{} pessoas ainda não atingiram a maior idade'.format(menor))
