velocidade = int(input('Qual a velocidade atual? '))
if velocidade > 80:
    print('Você foi multado em R${}'.format((velocidade - 80) * 7))