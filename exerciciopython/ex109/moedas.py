def aumentar(x = 0, taxa = 0, formato=False):
    """
    Função que calcula aumento percentual de um valor monetário informado.
    :param x: valor a ser aumentado.
    :param taxa: percentual de auemnto.
    :formato: formatação monetária (opcional)
    """
    res =  x + (x * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(x = 0, taxa = 0, formato=False):
    """
    Função que cálcula a diferença percentual de um valor monetário informado
    :param x: valor a ser subtraído
    :param taxa: percentual da diferença
    :formato: formatação monetária (opcional)
    """
    res =  x - (x * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(x = 0, formato=False):
    """
    Função que retorna o dobro de um valor monetário informado.
    :param x: valor a ser dobrado
    :param formato: formatação monetária (opcional)
    """
    res =  x * 2
    return res if not formato else moeda(res)


def metade(x = 0, formato=False):
    """
    Função que retorna a metade de um valor informado.
    :param x: valor que será repartido
    :param formato: formatação monetária (opcional)
    """
    res =  x / 2
    return res if not formato else moeda(res)

def moeda(x = 0, moeda = 'R$'):
    """
    Função que formata um valor monetário.
    :param x:
    :param moeda: por padrão, a moeda é o real
    """
    return f'{moeda}{x:>.2f}'.replace('.', ',')
