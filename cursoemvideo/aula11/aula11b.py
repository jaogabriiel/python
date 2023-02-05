nome = 'Gabriel'
cores = {'Limpa': '\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[0;30m'}
print('Olá! Muito prazer em te conhece, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['Limpa']))
