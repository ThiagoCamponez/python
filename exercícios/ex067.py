r = c = 0
n = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 35)
while True:
    while c <= 11:
        r = n * c
        print(f'{n} x {c} = {r}')
        c += 1
        if n < 0:
            break
        else:
            n = int(input('Quer ver a tabuada de qual valor? '))
print('Fim!')