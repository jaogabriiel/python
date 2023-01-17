extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
resp = ' '
while True:
    while True:
        print('-'*33)
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
    print(f'Você digitou o número {extenso[num]}')
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('Programa encerrado')
