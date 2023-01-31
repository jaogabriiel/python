números = list()
def maior(* núm):
    números.append(núm)
    print(f'Os números informados foram {números}')
    print(f'O maior número digitado foi {max(números[0])}')


maior(1, 5, 7, 4, 10, 6, 9, 20, 75, 14, 200)
