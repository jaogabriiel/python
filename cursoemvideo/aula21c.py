def teste():
    x = 8 # escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2 # escopo global
print(f'No programa proncipal, n vale {n}')
print(f'No programa principal, x vale {x}')
teste()
