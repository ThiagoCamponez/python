altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('IMC: {:.1f} - Abaixo do peso.'.format(imc))
elif imc < 25:
    print('IMC: {:.1f} - Peso ideal, PARABÉNS!.'.format(imc))
elif imc < 30:
    print('IMC: {:.1f} - Sobrepeso.'.format(imc))
elif imc < 40:
    print('IMC: {:.1f} - Obesidade.'.format(imc))
else:
    print('IMC: {:.1f} - Obesidade Mórbida! CUIDADO!'.format(imc))