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
print('-'*20)
print('N°', end=' ')
print('Aluno', end=' ')
print('Média')
print('-'*20)
for l, p in enumerate(pessoas):
    print(l, end=' ')
    print(p[0], end=' ')
    print((p[1] + p[2]) / 2) 

while True:
    mostrar = int(input('Quer ver os dados de qual aluno? (999 interrompe) '))
    if mostrar == 999:
        break
    for i in pessoas:
        print(i[mostrar])
print('Fim do programa')
