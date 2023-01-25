matriz = [[], [], []]
num1 = int(input('Digite um valor para [0, 0]: '))
num2 = int(input('Digite um valor para [0, 1]: '))
num3 = int(input('Digite um valor para [0, 2]: '))
num4 = int(input('Digite um valor para [1, 0]: '))
num5 = int(input('Digite um valor para [1, 1]: '))
num6 = int(input('Digite um valor para [1, 2]: '))
num7 = int(input('Digite um valor para [2, 0]: '))
num8 = int(input('Digite um valor para [2, 1]: '))
num9 = int(input('Digite um valor para [2, 2]: '))

matriz[0].append(num1)
matriz[0].append(num2)
matriz[0].append(num3)
matriz[1].append(num4)
matriz[1].append(num5)
matriz[1].append(num6)
matriz[2].append(num7)
matriz[2].append(num8)
matriz[2].append(num9)

print('A matriz 3x3 ficou assim: ')
for c in range(0 ,3):
    print(matriz[c])
