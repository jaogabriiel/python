lista = []
pessoas = []
while True:
    print('-='*20)
    nome = str(input('Nome: '))
    nota1 = float(input('Digite sua 1° nota: '))
    while nota1 > 10 or nota1 < 0:
        nota1 = float(input('Digite uma nota válida entre 0 e 10: '))
    nota2 = float(input('Digite sua 2° nota: '))
    while nota2 > 10 or nota2 < 0:
        nota2 = float(input('Digite uma nota válida entre 0 e 10: '))
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

print('-'*30)
print(f'{"N°":<4}', end=' ')
print(f'{"Aluno":<10}', end=' ')
print(f'{"Média":>8}')
print('-'*30)
for l, p in enumerate(pessoas):
    print(f'{l:<4}', end=' ')
    print(f'{p[0]:<10}', end=' ')
    print(f'{(p[1] + p[2]) / 2:>5}') 

while True:
    print('-='*30)
    mostrar = int(input('Quer ver os dados de qual aluno? (999 interrompe) '))
    if mostrar == 999:
        break
    while mostrar >= len(pessoas) or mostrar < 0:
        mostrar = int(input('Opção inválida.Tente novamente. '))
    print('='*50)
    print(f'Os dados do aluno {pessoas[mostrar][0]} são ', end=' ')
    print(pessoas[mostrar])
print('Fim do programa')
