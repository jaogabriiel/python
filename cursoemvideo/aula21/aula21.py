def contador(x, y, z):
    """
    Faz uma contagem e mostra na tela.
    :param x: início da contagem
    :param y: fim da contagem
    :param z: razão da contagem
    :return: sem retorno
    Função criada por João Gabriel afim de auxiliar o processo de contagem
    """
    c = x
    while c <= y:
        print(f'{c}', end=' ')
        c += z
    print('FIM')


help(contador)
