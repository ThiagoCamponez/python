reais = int(input('Valor em Reais: '))
cotacao = float(3.47)
dolar = reais / cotacao
print('O valor de {} reais, poderá comprar: {:.2f} dolares.'.format(reais, dolar))