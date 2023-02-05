import moedas

p = float(input('Digite um valor: R$'))
t = float(input('Taxa: '))
print(f'Aumentando {p} em {t}%, temos {moedas.aumentar(p, t, True)}')
print(f'Diminuindo {p} em {t}%, temos {moedas.diminuir(p, t)}')
print(f'O dobro de {p} é {moedas.dobro(p, True)}')
print(f'A metade de {p} é {moedas.metade(p)}')
