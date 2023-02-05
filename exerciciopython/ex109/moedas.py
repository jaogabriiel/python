def aumentar(x = 0, taxa = 0, formato=False):
    res =  x + (x * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(x = 0, taxa = 0, formato=False):
    res =  x - (x * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(x = 0, formato=False):
    res =  x * 2
    return res if not formato else moeda(res)


def metade(x = 0, formato=False):
    res =  x / 2
    return res if not formato else moeda(res)

def moeda(x = 0, moeda = 'R$'):
    return f'{moeda}{x:>.2f}'.replace('.', ',')
