primeiro = int(input('Digite um valor: '))
razão = int(input('Digite a razão da P.A: '))
termo = primeiro 
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo = termo + razão
    cont = cont + 1
print('Fim')
