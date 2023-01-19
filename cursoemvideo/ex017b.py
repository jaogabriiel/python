valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, valor in enumerate(valores):
    print(f'Na posição {c + 1} temos o valor {valor}')
print('Fim da lista')
