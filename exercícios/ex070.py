print('-' * 40)
print('LOJA SUPER BARATÃO'.center(40))
print('-' * 40)
total = 0
maiorquemil = 0
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    valor = float(input('Preço: R$'))
    total += valor
    if valor > 1000:
        maiorquemil += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print('------------- FIM DO PROGRAMA -------------')
print(f'O total da compra foi {total}')
print(f'Temos {maiorquemil} produtos custando mais de R$1000.00')