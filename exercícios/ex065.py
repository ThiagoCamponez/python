n = c = total = 0
continuar = 'S'
while continuar == 'S':
    c += 1
    n = int(input('Digite um número: '))
    total += n
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('Você digitou {} números e a média é {}'.format(c, total / c))