frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.upper().count('A')))
print('O primeiro "A" aparece na {}° posição'.format(frase.upper().find('A') + 1))
print('O último "A" aparece na {}° posição'.format(frase.upper().rfind('A') + 1))
