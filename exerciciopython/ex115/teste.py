arquivo = open('texto.txt', 'a')

frases = list()
frases.append('Python')
frases.append('Jg')
frases.append('Arquivod')

arquivo.writelines(frases)