primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão da P.A: '))
termo = primeiro 
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo = termo + razão
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão finalizada com {} termos'.format(total))
