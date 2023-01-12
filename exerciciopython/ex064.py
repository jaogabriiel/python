p = 1
soma = 0
cont = 0
while p != 999:
    p = float(input('Digite um número: '))
    if p != 999:
        soma = soma + p
        cont = cont + 1
print('Foram digitados {} números e a soma entre eles é {}'.format(cont, soma))
