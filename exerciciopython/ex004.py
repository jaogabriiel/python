dado = input('Digite algo:')
print('O tipo primitivo deste dado é', type(dado))
print('Só tem espaços? {}' .format(dado.isspace()))
print('É um número? {}' .format(dado.isnumeric()))
print('É alfabético? {}' .format(dado.isalpha()))
print('É alfanumérico? {}' .format(dado.isalnum()))
print('Está só em maiúsculas? {}' .format(dado.isupper()))
print('Está so em minúsculas? {}' .format(dado.islower()))
print('Está capitalizada? {}' .format(dado.istitle()))