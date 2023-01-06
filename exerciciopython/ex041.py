from datetime import date
nas = int(input('Digite seu ano de nascimento para informarmos sua categoria: '))
atual = date.today().year
idade = atual - nas
if idade <= 9:
    categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 19:
    categoria = 'JUNIOR'
elif idade > 19 and idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('Com {} anos sua categoria é {}'.format(idade, categoria))
