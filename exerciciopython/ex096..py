def área(x, y):
    area = x * y
    print(f'Com uma dimensão {largura}x{comprimento} m² a área do terreno é {area}m²')


print('Controle de Terrenos')
print('-'*25)
largura = float(input('Largura do terreno (m): '))
comprimento = float(input('Comprimento do terreno (m): '))
área(largura, comprimento)
