pessoas = {'nome': 'Gabriel', 'sexo': 'M', 'idade': 19}
del pessoas['sexo']
pessoas['nome'] = 'Rose'
pessoas['peso'] = '104'
for k, v in pessoas.items():
    print(f'{k} = {v}')
