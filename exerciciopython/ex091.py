from random import randint
from operator import itemgetter
from time import sleep
jogadores = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}
for k, c in jogadores.items():
    print(f'{k} tirou {c}')
    sleep(1)
ranking = list()
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
