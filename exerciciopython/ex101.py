from datetime import date
def voto(x):
    idade = date.today().year - x
    if idade < 18:
        return 'NÃO VOTA'
    elif 18 <= idade < 65:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'

ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
print(f'Com {idade} voto: {voto(ano)}')
