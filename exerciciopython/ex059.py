from time import sleep
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
opção = 0
while opção != 5:
    print('''   
[1] SOMAR
[2] MULTIPLICAR
[3] O MAIOR VALOR
[4] NOVOS VALORES
[5] SAIR:''')   
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O produto entre {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    sleep(1)
print('Fim do programa')
