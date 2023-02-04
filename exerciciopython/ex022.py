nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em maiúsculas: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))
print('O nome possui um total de {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()

print('Seu primeiro nome é {} e possui {} letras'.format(dividido[0], len(dividido[0])))
