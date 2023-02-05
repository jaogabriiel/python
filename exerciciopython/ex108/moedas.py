def aumentar(x = 0, taxa = 0):
    res =  x + (x * taxa / 100)
    return res


def diminuir(x = 0, taxa = 0):
    res =  x - (x * taxa / 100)
    return res


def dobro(x = 0):
    res =  x * 2
    return res


def metade(x = 0):
    res =  x / 2
    return res

def moeda(x = 0, moeda = 'R$'):
    return f'{moeda}{x:>.2f}'.replace('.', ',')
