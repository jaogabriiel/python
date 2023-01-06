valor = float(input('Valor da casa: R$'))
salário = float(input('Salário: R$'))
anos = int(input('Anos de financiamento: '))
prestação = valor / (anos * 12)
if prestação > salário * 30 / 100:
    emprestimo = 'NEGADO!'
else:
    emprestimo = 'CONCEDIDO!'
print('Para pagar uma casa de {} em  {} anos a prestação será de R${:.2f}'.format(valor, anos, prestação))
print('Emprestimo {}'.format(emprestimo))
