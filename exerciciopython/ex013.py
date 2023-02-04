salário = float(input('Digite seu salário: R$'))
aumento = 15 / 100 * salário
salario_final = salário + aumento
print('Seu salário de {}R$ com um aumento de 15% é de {:.1f}R$'.format(salário, salario_final))
