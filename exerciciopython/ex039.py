from datetime import date

veri = str(input('Qual seu sexo? Digite 0 para MASCULINO e 1 para FEMININO: '))

if veri == '0':
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    if idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('Com {} anos você se alistará no exército daqui a {} anos'.format(idade, 18 - idade))
        print('Seu alistamento será em {}'.format(ano))
    elif idade == 18:
        print('Com 18 anos você já deve estar alistado!')
    else:
        saldo = idade - 18
        ano = atual - saldo
        print('Com {} anos você se alistou no exército há {} anos'.format(idade, idade - 18))
        print('Seu alistamento foi em {}'.format(ano))
elif veri == '1':
    print('Você não participa do alistamento obrigatório')
else:
    print('Digite um número válido')
