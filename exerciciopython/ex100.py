from random import randint
sorteados = list()
pares = list()
def sorteio():
    for c in range(1, 6):
        sorteados.append(randint(1, 10))
    print(f'Os números sorteados foram {sorteados}')
    
def soma_pares():
    for v in sorteados:
        if v % 2 == 0:
            pares.append(v) 
    print(f'Os números pares sorteados foram {pares} e a soma deles é {sum(pares)}')

sorteio()
soma_pares()
