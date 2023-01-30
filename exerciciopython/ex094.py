pessoas = list()
cada = dict()
mulheres = list()
acima = list()
somaidade = 0
while True:
    print('=-'*40)
    cada['nome'] = str(input('Nome: '))
    cada['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while cada['sexo'] not in 'MmFf':
        print('ERRO. Digite apenas M ou F')
        cada['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if cada['sexo'] in 'Ff':
        mulheres.append(cada['nome'])
    cada['idade'] = int(input('Idade: '))
    somaidade += cada['idade']
    pessoas.append(cada.copy())
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp not in 'sn':
        print('ERRO. Digite apenas S ou N.')
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break
print('-'*40)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas')
média = somaidade / len(pessoas)
print(f'A média de idade do grupo é {média}')
print(f'As mulheres cadastradas foram', end=' ')
for i in mulheres:
    print(i, end=' ')
for i, v in enumerate(pessoas):
    if v['idade'] > média:
        acima.append(v['nome'])
print(f'\nAs pessoas com idade acima da média são {acima}')
