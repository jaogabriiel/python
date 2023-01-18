n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último valor: '))
números = (n1, n2, n3, n4)
print(f'Os números digitados foram {números}')
print(f'O número 9 apareceu {números.count(9)} vezes')
if 3 in números:
    print(f'O número 3 apareceu primeiramente na {números.index(3) + 1}° posição')
else:
    print('O valor 3 não foi encontrado')
print('Os valores pares digitados foram: ', end='')
for n in números:
    if n % 2 == 0:
        print(n, end=' ')
