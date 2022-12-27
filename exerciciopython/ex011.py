lar = int(input('Digite a largura da parede: '))
alt = int(input('Digite a altura da parede: '))
area = lar * alt
qtdTinta = area / 2
print('Você vai precisar de {} litros de tinta para pintar a parede'.format(qtdTinta))