lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]
    elif lista[c] < menor:
        menor = lista[c]

print('=-'*20)
print(lista)
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}', end=' ')
print(f'\nO menor valor digitador foi {menor} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}', end=' ')
