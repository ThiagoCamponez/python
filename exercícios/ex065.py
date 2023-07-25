n = c = total = maior = menor =  0
continuar = 'S'
while continuar == 'S':
    c += 1
    n = int(input('Digite um número: '))
    total += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('Você digitou {} números e a média é {:.2f}'.format(c, total / c))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))