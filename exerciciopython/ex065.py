res = 'S'
média = soma = quant = maior = menor = 0
while res in 'Ss':
    núm = int(input('Digite um número: '))
    soma = soma + núm
    quant = quant + 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor digitado foi {} e o menor {}'.format(maior, menor))
