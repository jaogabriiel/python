soma = cont = 0
while True:
    n = int(input('Digite um número (999 para encerrar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Ao todo foram informados {cont} números e a soma deles é {soma}')
