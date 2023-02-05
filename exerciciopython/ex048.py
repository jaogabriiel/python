soma = 0
cont = 0 
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma = soma + c
        
print('A soma dos {} valores entre 1 e 500 que são múltiplos de 3 é {}'.format(cont, soma))
