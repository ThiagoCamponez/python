distancia = float(input('Quantos km é a distância da sua viagem: '))
if distancia < 201:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Sua passagem terá o valor de R${:.2f}'.format(preço))