def ficha(txt, x):
    if len(txt) == 0:
        return 'desconhecido' 
    elif len(txt) != 0:
        return txt
    
    if len(x) == 0:
        return 0
    else:
        return x
    

nome = str(input('Nome do jogador: '))
gols = int(input('Quantidade de gols: '))
print(ficha(nome, gols))
# print(f'O jogador {ficha(nome)} fez {ficha(gols)} gols')
