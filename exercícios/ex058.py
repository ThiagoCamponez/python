from random import randint
tentativas = 0
computador = randint(0, 10)
print('-' * 70)
print('Sou seu computador! Adivinhe o número que estou pensando entre 0 e 10.')
print('-' * 70)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\nQual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
print('\nVocê acertou com {} tentativas. Parabéns!'.format(palpites))
