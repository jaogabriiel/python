times  = ('Corinthians', 'Atlético-MG', 'Grêmio', 'São Paulo', 
          'Sport','Santos', 'Cruzeiro', 'Palmeiras', 
          'Atlético-PR', 'Ponte Preta', 'Flamengo', 'Fluminense', 'Chapecoense', 'Coritiba', 'Figueirense', 'Avaí',
          'Vasco', 'Goiás', 'Joinville')
print('='*94)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('='*94)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('='*94)
print(f'times em ordem alfabética: {sorted(times)}')
print('='*94)
print(f'O sport está na {times.index("Sport") + 1}ª colocação')
