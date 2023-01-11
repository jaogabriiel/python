from random import randint
escolhido = randint(0, 10)
cont = 0
tentativa = int(input('O computador pensou em um número. Tente adivinhar: '))
while tentativa != escolhido:
    tentativa = int(input('Você errou! tente novamente: '))
    cont = cont + 1
print('Acertou! Pensei no número {}. Você precisou de {} tentativas'.format(escolhido, cont))
