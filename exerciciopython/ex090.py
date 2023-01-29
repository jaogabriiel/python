boletim = dict()
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input('Média final: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'
    
print('-='*20)
for i, v in boletim.items():
    print(f'{i} é igual a {v}')
