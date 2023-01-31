from time import sleep
def linha():
    print('-='*30)
def contador():
    print('Contagem de 1 a 10, de 1 em 1:')
    for c in range(1, 11):     
        print(c, end=' ')
    print('\nContagem de 10 a 0, de 2 em 2')
    for c in range(10, -1, -2):
        print(c, end=' ')
    print('\nAGORA É SUA VEZ!')
    início = int(input('Início da contagem: '))
    final = int(input('Final da contagem: '))
    passo = int(input('Passo: '))
    if passo == 0:
        print('[ERRO]. Será considerado passo 1')
        passo = 1
    if passo < 0:
        passo = passo * (-1)
        print(f'Será considerado passo {passo}')
    if início > final:
        passo *= -1
    for c in range(início, final + 1, passo):
        print(c, end=' ') 
    
        
contador()