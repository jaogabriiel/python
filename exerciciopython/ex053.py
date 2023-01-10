frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso da frase é {}'.format(inverso).lower())
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
