def notas(* notas, sit=False):
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