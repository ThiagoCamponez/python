distancia = int(input('Quantos km é a distância da sua viagem: '))
if distancia < 201:
    print('Sua passagem custará R${:.2f}'.format(distancia * 0.50))
else:
    print('Sua passagem terá o valor de R${:.2f}'.format(distancia * 0.45))