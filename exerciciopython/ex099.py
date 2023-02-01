from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-' * 50)
    print('\nAnalisando os valores passados...')
    for v in núm:
        print(v, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'\nAo todo foram informados {cont} valores e o maior é {maior}')

maior(1, 5, 7, 4, 10, 6, 9, 20, 75, 14, 200)
maior(2, 7, 63, 45, 78, 20)
