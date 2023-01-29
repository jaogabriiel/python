dados = {}
gols = []
cont = 1
soma = 0
while True:
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Números de partidas: '))
    while cont <= partidas:
        golsp = int(input(f'Gols na {cont} partida: '))
        gols.append(golsp)
        soma = soma + golsp
        dados['gols'] = gols
        cont += 1
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('fim')