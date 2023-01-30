dados = dict()
gols = list()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Número de partidas: '))
cont = 1
while cont <= partidas:
    golsp = int(input(f'Gols feitos na {cont}° partida: '))
    gols.append(golsp)
    cont += 1
dados['gols'] = gols
dados['total'] = sum(gols)
print(dados)
for i, v in dados.items():
    print(f'O campo {i} tem valor {v}.')

print('-='*30)
print(f'O {dados["nome"]} jogou {partidas} partidas')
for i, g in enumerate(gols):
    print(f'=> Na {i + 1}° partida, {dados["nome"]} fez {gols[i]} gols')
print(f'Foi um total de {dados["total"]} gols')
