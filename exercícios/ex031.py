distancia = float(input('Quantos km é a distância da sua viagem: '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Sua passagem terá o valor de R${:.2f}'.format(preço))