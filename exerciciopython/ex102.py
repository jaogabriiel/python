def fatorial(x, show=False):
    f = 1
    for c in range(x, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f

print(fatorial(10, True))
