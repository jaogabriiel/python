lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Organiza em ordem alfabética
print(sorted(lanche)) 
print(lanche)

# Aqui não é possível adicionar a posição dos elementos
for comida in lanche:
    print(f'Eu vou comer {comida}')
    
# Aqui consegumos mostrar a posição dos elementos
for cont in range(0, len(lanche)):
    print(f'Em {cont} lugar vou comer {lanche[cont]}')

# Aqui consegumos mostrar a posição dos elementos
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
