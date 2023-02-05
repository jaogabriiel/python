import moedas

p = float(input('Digite um valor: R$'))
t = float(input('Taxa: '))
print(f'Aumentando {moedas.moeda(p)} em {t}%, temos {moedas.moeda(moedas.aumentar(p, t))}')
print(f'Diminuindo {moedas.moeda(p)} em {t}%, temos {moedas.moeda(moedas.diminuir(p, t))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
