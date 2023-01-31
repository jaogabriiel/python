def área():
    print('Controle de Terrenos')
    print('-'*25)
    largura = float(input('Largura do terreno (m): '))
    comprimento = float(input('Comprimento do terreno (m): '))
    area = largura * comprimento
    print(f'Com uma dimensão {largura}x{comprimento} m² a área do terreno é {area}m²')


área()