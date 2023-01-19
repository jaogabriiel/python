palavras = ('Música', 'Programar', 'Trabalho', 'Tecnologia', 'Futuro', 'Bíblia', 'Igreja', 'Cristo', 'Computador', 'Notebook', 'Dinheiro', 'Família')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ') 
