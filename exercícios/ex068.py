from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(30))
print('=-' * 15)
qtdVitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    parImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = computador + jogador
    deu = ''
    vencedor = ''
    if soma % 2 == 0:
        deu = 'PAR'
        if parImpar == 'P':
            vencedor = 'Você VENCEU!\nVamos jogar novamente...'
            qtdVitorias += 1
        else:
            vencedor = 'Você PERDEU..'
            break
    else:
        deu = 'ÍMPAR'
        if parImpar == 'I':
            vencedor = 'Você VENCEU!\nVamos jogar novamente...'
            qtdVitorias += 1
        else:
            vencedor = 'Você PERDEU..'
            break
    print('-' * 60)
    print(f'Você jogou {jogador} e o Computador {computador}. Total de {soma}, DEU **{deu}**'.center(60))
    print('-' * 60)
    print(vencedor)
    print('=-' * 16)
print('-' * 60)
print(f'Você jogou {jogador} e o Computador {computador}. Total de {soma}, DEU **{deu}**'.center(60))
print('-' * 60)
print(vencedor)
print('=-' * 16)
print(f'GAME OVER! Você venceu {qtdVitorias} vezes.' if vencedor == 'Você PERDEU..' else '')