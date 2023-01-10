primeiro = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))
décimo = primeiro + (10 - 1) * razão
print('Os 10 primeiros termos da P.A são: ')
for c in range(primeiro, décimo + razão, razão):
    print(c, end='-> ')
print('Fim')
