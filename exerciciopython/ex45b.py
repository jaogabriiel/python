from random import randint
from time import sleep
intens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')

jogador = int(input('qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 15)
print('O computador jogou {}'.format(intens[computador]))
print('O jogador jogou {}'.format(intens[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('EU GANHEI ksksksksk')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('EU GANHEI kskskssksk')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Você ganhou!')
    else:
        print('Jogada inválida')
    
elif computador == 2:
    if jogador == 0:
        print('Você ganhou')
    elif jogador == 1:
        print('EU GANHEI kskskksks')
    elif jogador == 2:
        print('EMAPTE')
    else:
        print('Jogada inválida')
