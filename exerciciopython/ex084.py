pessoas = list()
dados = list()
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    dados.append(nome)
    peso = float(input('Peso: '))
    dados.append(peso)
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break

print('='*40)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg, que foi o peso do(a)', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}Kg, que foi o peso do(a)', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}')
