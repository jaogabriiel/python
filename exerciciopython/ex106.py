
c = ('\033[m' , # sem cor 
     '\033[0;30;41m', # vermelho
     )
def ajuda(msg):
    help(msg)

def tútulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor] , end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    
opção = ''
while True:
    tútulo('SISTEMA DE AJUDA PyHELP', 1)
    opção = str(input('Função ou Biblioteca: '))
    if opção.upper() == 'FIM': 
        break
    else:
        ajuda(opção)
tútulo('Até a próxima', 1)