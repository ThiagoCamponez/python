dias = int(input('Por quantos dias ele foi alugado: '))
km = float(input('Quantos km percorreu com o carro: '))
total = (dias * 60) + (km * 0.15)
print('Total a pagar = R${:.2f}'.format(total))