maior18 = 0
homem = 0
mulher20 = 0
while True:
    print('-'*30)
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'M':
        homem += 1
    if sexo in 'M':
        if idade < 20:
            mulher20 += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opção in 'N':
        break
print('-'*30)
print(f'Ao todo, {maior18} pessoas têm mais de 18 anos')
print(f'foram cadastrados {homem} homens')
print(f'{mulher20} mulheres têm menos de 20 anos')
