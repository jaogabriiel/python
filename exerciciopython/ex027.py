nome = str(input('Digite seu nome completo: ')).strip()
partido = nome.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(partido[0]))
print('Seu último nome é {}'.format(partido[len(partido) - 1]))
