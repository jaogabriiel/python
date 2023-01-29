pessoas = list()
cada = dict()
mulheres = list()
acima = list()
somaidade = 0
while True:
    cada['nome'] = str(input('Nome: '))
    cada['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while cada['sexo'] not in 'MmFf':
        cada['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if cada['sexo'] in 'Ff':
        mulheres.append(cada['nome'])
    cada['idade'] = int(input('Idade: '))
    somaidade = cada['idade'] + somaidade
    pessoas.append(cada)
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break
média = somaidade / len(pessoas)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas')
print(f'A média de idade do grupo é {média}')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'As pessoas com idade acima da média são {acima}')
