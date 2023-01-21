lista = []
resp = ' '
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado')
    else:
        print('O número já está na lista. Não será considerado')
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
lista.sort()
print(f'Os números informados foram {lista}')
