from random import randint
from time import sleep
tentativas = 0
computador = randint(0, 11)
print('-' * 70)
print('Sou seu computador! Adivinhe o número que estou pensando entre 0 e 10.')
print('-' * 70)
jogador = int(input('\nQual é o seu palpite? '))
sleep(1)
while computador != jogador:
    if computador > jogador:
        print('\nÉ mais... Tente novamente!')
        tentativas += 1
        sleep(1)
        jogador = int(input('\nQual é o seu palpite? '))
    elif computador < jogador:
        print('\nÉ menos... Tente novamente!')
        tentativas += 1
        sleep(1)
        jogador = int(input('\nQual é o seu palpite? '))
print('\nVocê acertou com {} tentativas. Parabéns!'.format(tentativas))