from random import randint
from time import sleep
sorteado = randint(1, 3)
if sorteado == 1:
    computador = 'PEDRA'
elif sorteado == 2:
    computador = 'PAPEL'
else:
    computador = 'TESOURA'
    
usuário = int(input('''Vamos jogar Jokenpô? 
[1] para PEDRA
[2] para PAPEL
[3] para TESOURA
faça sua jogada: '''))
if usuário == 1:
    jogador = 'PEDRA'
elif usuário == 2:
    jogador = 'PAPEL'
elif usuário == 3:
    jogador = 'TESOURA'
else:
    print('Jogada inválida!')
    
if sorteado == usuário:
    resultado = 'EMPATE'
else:
    if sorteado == 1 and usuário == 2:
        resultado = 'Você ganhou! affs'
    elif sorteado == 1 and usuário ==3:
        resultado = 'EU GANHEI KKKKKKLSDSA'
    elif sorteado == 2 and usuário == 1:
        resultado = 'EU GANHEI LKKKKKKKKSK'
    elif sorteado == 2 and usuário == 3:
        resultado = 'Você ganhou! affs'
    elif sorteado == 3 and usuário == 1:
        resultado = 'Você ganhou! affs'
    elif sorteado == 3 and usuário == 2:
        resultado = 'EU GANHEI KKKLLSSPKASPKDAS'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('Eu joguei {} e você {}'.format(computador, jogador))
print(resultado)
