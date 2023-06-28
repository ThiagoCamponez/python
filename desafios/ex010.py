reais = float(input('Valor em Reais: R$'))
dolar = reais / 3.27
print('Com o valor de R${:.2f}, você poderá comprar: US${:.2f} '.format(reais, dolar))