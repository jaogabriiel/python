import random
num = random.randint(0, 5)
chute = int(input('O computador acabou de pensar um um número, será que você consegue adivinhá-lo? '))
if chute == num:
    print('PARABÉNS! Você acertou o número!')
else:
    print('Que pena! Esse não foi o número pensado pelo computador!')
