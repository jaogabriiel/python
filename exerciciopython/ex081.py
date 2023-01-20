lista = []
while True:
    print('='*20)
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não foi encontrado')
