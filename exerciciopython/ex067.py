while True:
    n = int(input('Digite um número e veja sua tabuada: '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {c * n}')
    print('-'*30)
print('Fim do gerador de tabuada')
