jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Número de partidas jogadas por {jogador["nome"]}: '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Gols na partida {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Responda apenas S ou N')
    if resp == 'N':
        break
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO. Não existe jogador com o código {busca}')
    else:
        print(f'   Levanatamento dp jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-=' * 30)
print('<< VOLTE SEMPRE >>')
