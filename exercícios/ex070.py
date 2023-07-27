print('-' * 40)
print('LOJA SUPER BARATÃO'.center(40))
print('-' * 40)
total = menor = menorvalor = maiorquemil = 0
produtomenorvalor = ''
while True:
    menor += 1
    produto = str(input('Nome do Produto: ')).strip().upper()
    valor = float(input('Preço: R$'))
    total += valor
    if valor > 1000:
        maiorquemil += 1
    if menor == 1:
        menorvalor = valor
        produtomenorvalor = produto
    else:
        if valor < menorvalor:
            menorvalor = valor
            produtomenorvalor = produto
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print('------------- FIM DO PROGRAMA -------------')
print(f'O total da compra foi {total}')
print(f'Temos {maiorquemil} produtos custando mais de R$1000.00')
print(f'E o produto mais barato foi: {produtomenorvalor} que custa R${menorvalor}')