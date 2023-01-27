from datetime import date
atual = date.today().year
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = atual - nasc
dados['Carteira'] = int(input('Carteira de trabalho (0 não tenho): '))
if dados['Carteira'] != 0:
    dados['Contratação'] = int(input('Ano de contratração: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Contratação'] + 35
    for i, v in dados.items():
        print('='*30)
        print(f'O {i} tem valor {v}')
else:
    for i, v in dados.items():
        print('='*30)
        print(f'O {i} tem valor {v}')
