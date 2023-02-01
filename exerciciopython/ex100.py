from random import randint
from time import sleep
sorteados = list()
def sorteio(lista):
    print('Sorteando os valores')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)

    
def soma_pares(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares de {lista} obtemos {soma}')
           
            
sorteio(sorteados)
soma_pares(sorteados)
