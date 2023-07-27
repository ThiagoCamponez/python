from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(30))
print('=-' * 15)
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 55)
    print(f'Você jogou {jogador} e o Computador {computador}. Total de {total} ', end= '')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-' * 55)
    if tipo  == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU..')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU..')
            break
    print('Vamos jogar novamente...')
    print('=-' * 16)
print('=-' * 16)
print(f'GAME OVER! Você venceu {v} vezes.')