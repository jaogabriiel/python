from time import sleep
def contador(x, y, z):
    if z < 0:
        z *= -1
    if z == 0:
        print('[ERRO] Será comsiderado a razão 1')
        z = 1
    print('-='*20)
    print(f'Contagem de {x} até {y} de {z} em {z}:')
    if x < y:
        sleep(1)
        for c in range(x, y + 1, z):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    elif x >= y:
        for c in range(x, y - z , -z):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez! Vamos personalizar a contagem')
ini = int(input('Início da contagem:   '))
fim = int(input('Final da contagem:   '))
passo = int(input('Razão da contagem:   '))
contador(ini, fim, passo)
