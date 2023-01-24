lista = []
pessoas = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    pessoas.append(lista[:])
    lista.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break
print(pessoas)
print('N°', end=' ')
print('Nome', end=' ')
print('Média')

