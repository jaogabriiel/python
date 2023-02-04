real = float(input('Quanto você tem? R$'))
dolar = real / 5.22
euro = real / 5.63
libra = real / 6.73
bitcoin = real / 88.289
print('Você pode comprar {:.2f}US$ de Dólar \n{:.2f} Euros \n{:.2f} Libras e \n{:.2f} Bitcoins'.format(dolar, euro, libra, bitcoin))
