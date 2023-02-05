def dobro(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
print(valores)
dobro(valores)
print(valores)
