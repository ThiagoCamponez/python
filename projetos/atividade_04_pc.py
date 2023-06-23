listaCarros = []
listaConsumo = []
quantidade = int(input(f'Lista de quantos carros? '))
for i in range(quantidade):
    carro = str(input(f'Digite um modelo do {i+1}º carro: '))
    listaCarros.append(carro)
    km = float(input('Qual o consumo do carro {},(km/l)? '.format(carro)))
    listaConsumo.append(km)

distancia = 500
valorGasolina = 4.9

for i in range(quantidade):
    litros = distancia / listaConsumo[i]
    custo = litros * valorGasolina
    print('========================================================================')
    print('O carro {}, gastará {:.2f} litros de gasolina, para percorrer 500km.'.format(listaCarros[i], litros))
    print('Com a gasolina a R$4,90 você terá um custo de R${:.2f} para esta viagem!'.format(custo))
