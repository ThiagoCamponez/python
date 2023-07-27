while True:
    num = int(input('\nQuer ver a tabuada de qual valor? '))
    print('-' * 35)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 35)
print('\nPrograma Tabuada ENCERRADO. Volte sempre!\n')