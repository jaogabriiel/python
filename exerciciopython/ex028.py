from random import randint
from time import sleep
num = randint(0, 5)
chute = int(input('Vou pensar em um número entre 0 e 5, será que você consegue adivinhá-lo? '))

if chute == num:
    print('Espera aí rapidinho...')
    sleep(2)
    print('PARABÉNS! Você acertou o número!')
else:
    print('Espera aí rapidinho...')
    sleep(2)
    print('EU GANHEI! Eu pensei no {} e não no {}. você errou kkkkkkkj'.format(num, chute))
