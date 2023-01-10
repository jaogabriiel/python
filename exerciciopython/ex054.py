from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    ano = int(input('Em que ano a  {}° pessoa nasceu? '.format(pess)))
    idade = atual - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoas já atingiram a maior idade'.format(maior))
print('{} pessoas ainda não atingiram a maior idade'.format(menor))
