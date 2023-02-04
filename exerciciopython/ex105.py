def notas(* notas, sit=False):
    """
    Função que recebe recebe notas como parâmetro e retorna algumas informações, como:
    -> Número de notas informadas
    -> Maior nota
    -> Menor nota
    -> A média entre as notas
    -> A situação (opcional)
    """
    n = dict()
    n['total'] = len(notas)
    n['maior'] = max(notas)
    n['menor'] = min(notas)
    n['média'] = sum(notas) / len(notas)
    if sit:
        if n['média'] > 7:
            n['sit'] = 'Bom'
        elif 6 < n['média'] < 7:
            n['sit'] = 'Razoável'
        else:
            n['sit'] = 'Ruim'
    return n

resp = notas(4, 8.5, 9.3, 10, sit=True)
print(resp)
help(notas)