def leiaInt(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m[ERRO] Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário\033[m]')
            return 0
        else:
            return i
    

def leiaReal(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m[ERRO] Digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário\033[m]')
            return 0
        else:
            return r
