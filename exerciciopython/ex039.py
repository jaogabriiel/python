from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade < 18:
    print('Com {} anos você se alistará no exército daqui a {} anos'.format(idade, 18 - idade))
elif idade == 18:
    print('Com 18 anos você já deve estar alistado!')
else:
    print('Com {} anos você se alistou no exèrcito há {} anos'.format(idade, idade - 18))
