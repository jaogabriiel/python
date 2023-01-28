dados = dict()
gols = list()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Número de partidas: '))
cont = 1
soma = 0
while cont <= partidas:
    golsp = int(input(f'Gols feitos na {cont}° partida: '))
    gols.append(golsp)
    soma = soma + golsp
    cont += 1
dados['gols'] = gols
dados['total'] = soma
print(dados)
for i, v in dados.items():
    print(f'O campo {i} tem valor {v}.')

print('-='*30)
print(f'O {dados["nome"]} jogou {partidas} partidas')
