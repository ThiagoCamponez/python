res = 0
num = 1
while num > 0:
    num = int(input('\nQuer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 35)
    cont = 1
    while cont <= 10:
        res = num * cont
        print(f'{num} x {cont} = {res}')
        cont += 1
    print('-' * 35)
print('\nPrograma Tabuada ENCERRADO. Volte sempre!\n')