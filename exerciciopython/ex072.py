extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
           'Dezenove', 'Vinte')
resp = ' '
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while True:
        if 0 <= num <= 20:
            break
        else:
            num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você didigitou o número {extenso[num].upper()}')
    print('='*30)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('Programa encerrado')
