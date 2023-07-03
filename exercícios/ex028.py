from random import choice
lista = [1, 2, 3, 4, 5]
sorteado = choice(lista)
num = int(input('Adivinhe qual número de 1 à 5 será sorteado: '))
if num == sorteado:
    print('Parabéns! Você escolheu o número sorteado! Foi o {}!'.format(sorteado))
else:
    print('Que pena, você escolheu o {}, mas o número sorteado foi {}.'.format(num, sorteado))