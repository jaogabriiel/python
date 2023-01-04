lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
qtd_tinta = area / 2
print('A dimensão da parede é {}x{} com uma áre de {:.2f}m², você precisará de {:.2f}l de tinta para pintar a parede'.format(lar, alt, area, qtd_tinta))
