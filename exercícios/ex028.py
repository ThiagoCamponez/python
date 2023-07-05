from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
print('=-^-' * 14)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-^-' * 14)
jogador = int(input('Qual número eu pensei? ')) #jogador tenta adivinhar
print('Pensando...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você consegui me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}.'.format(computador, jogador))