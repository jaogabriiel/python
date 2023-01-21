num = []
pares = []
ímpares = []
while True:
    valor = int(input('Digite um valor: '))
    num.append(valor)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break
print('='*25)
print(f'Os valores digitados foram {num}')
for c in num:
    if c % 2 == 0:
        pares.append(c)
    else:
        ímpares.append(c)
print(f'Pares: {pares}')
print(f'Ímpares: {ímpares}')
