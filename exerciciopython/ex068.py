from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    commputador = randint(0, 10)
    total = commputador + jogador
    tipo = ' ' 
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {commputador} o total é {total}')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes')
