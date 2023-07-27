print('-' * 40)
print('LOJA SUPER BARATÃO'.center(40))
print('-' * 40)
total = menor = menorvalor = totmil = 0
produtomenorvalor = ''
while True:
    menor += 1
    produto = str(input('Nome do Produto: ')).strip().upper()
    valor = float(input('Preço: R$'))
    total += valor
    if valor > 1000:
        totmil += 1
    if menor == 1 or valor < menorvalor:
        menorvalor = valor
        produtomenorvalor = produto
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'E o produto mais barato foi: {produtomenorvalor} que custa R${menorvalor:.2f}')