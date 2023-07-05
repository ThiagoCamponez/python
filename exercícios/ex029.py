print('-' *40)
print('Qual a velocidade atual do automóvel? ')
print('-' *40)
velocidade = int(input('km/h:  '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80 km/h.')
    print('Você deve pagar uma multa de R${},00'.format((velocidade - 80) * 7))
print('Tenha uma ótima viagem e digija com segurança!')