a = [2, 3, 4, 7]
#b = a  as listas ficam iguais
b = a[:] # cria uma cópia de A em B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
