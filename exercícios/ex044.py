print(' LOJAS CAMPONÊZ '.center(30, '='))
preçoNormal = float(input('Valor dos produtos: '))
condPagamento = int(input('\n[1] À Vista dinheiro/cheque - 10% de desconto\n[2] À Vista no cartão de débito - 5% de desconto\n[3] Em até 2x no cartão de crédito - Valor normal\n[4] 3x ou mais no cartão de crédito - 20% de Juros\n\nInforme a condição de pagamento: '))
print('\nValor do produto: R${:.2f}'.format(preçoNormal), end = ' ')
if condPagamento == 1:
    print(', Valor com 10% de desconto: R${:.2f}\n'.format(preçoNormal - (preçoNormal * 10 / 100)))
elif condPagamento == 2:
    print(', Valor com 5% de desconto: R${:.2f}\n'.format(preçoNormal - (preçoNormal * 5 / 100)))
elif condPagamento == 3:
    parcelas = int(input(', Quantas vezes: '))
    if parcelas == 1:
        print('\nValor normal: R${:.2f}'.format(preçoNormal))
    elif parcelas == 2:
        print('\nEntão ficará 2x de R${:.2f}'.format(preçoNormal / 2))
elif condPagamento == 4:
    pcJuros = preçoNormal + (preçoNormal * 20 / 100)
    print(', Valor com 20% de juros ficará: R${:.2f}'.format(pcJuros))
    parcelas = int(input('\nQuantas parcelas: '))
    print('\nEntão ficará {} parcelas de R${:.2f}, Total de R${:.2f}'.format(parcelas, pcJuros / parcelas, pcJuros))
