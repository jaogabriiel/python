produtos = ('Pão', 1.0, 
            'Leite', 4.0, 
            'Ovos', 0.50, 
            'Biscoito', 2.0, 
            'Bolacha', 3.0, 
            'Carne', 10.0, 
            'Feijão', 5.0)
print('='*41)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R${produtos[pos]:>7.2f}')
