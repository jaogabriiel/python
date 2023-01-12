n = int(input('Digite um número e veja seu fatorial: '))
c = n
f = 1
print('Claculando {}!'.format(n), end= ' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c = c - 1
print('{}'.format(f))

# n = int(input('digite o numero '))
# f = 1
# for c in range(n, 0, -1):
#     print(c ,end=' ')
#     print('x' if c > 1 else '=',end=' ')
#     f = f *  c
# print('{}'.format(f),end='')
