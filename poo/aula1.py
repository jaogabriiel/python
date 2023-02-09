class Carro:
    velMax = 0
    ligado = False
    cor = ''
    
c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax = 200
c1.cor = 'Preto'
c1.ligado = False

print(f'Velocidade máxima: {c1.velMax}')
print(f'Cor: {c1.cor}')
estado = 'Sim' if c1.ligado == True else 'Não'
print(f'Ligado: {estado}')
