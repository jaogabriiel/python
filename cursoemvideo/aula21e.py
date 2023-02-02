def somar(x = 0, y = 0, z = 0):
    s = x + y + z
    return s
    
r1 = somar(3, 2, 5) # o 'S' em return vai para dentro da variável 'r1'
r2 = somar(2, 2)
r3 = somar(10)

print(f'Os resultados foram {r1}, {r2} e {r3}')
