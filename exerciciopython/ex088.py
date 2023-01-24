from random import randint
lista = list()
jogos = list()
qtd = int(input('Quantidade de jogos a serem sorteados: '))
total = 0
while total <= qtd - 1:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1} : {j}')
