from random import choice
jogador = str(input('Digite seu nome: ')).strip().upper()
apostaJogador = str(input('Pedra, Papel ou Tesoura: ')).strip().lower()
if apostaJogador != ['pedra', 'papel', 'tesoura']:
    apostaJogador = str(input('Escolha inválida! Pedra, Papel ou Tesoura: '))
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
print('{}: {}, COMPUTADOR: {} ---> VENCEDOR É O'.format(jogador, apostaJogador, computador), end = ' ')
if apostaJogador == 'pedra' and computador == 'papel':
    print('COMPUTADOR!')
elif apostaJogador == 'pedra' and computador == 'tesoura':
    print('{}'.format(jogador))
elif apostaJogador == 'papel' and computador == 'pedra':
    print('{}'.format(jogador))
elif apostaJogador == 'papel' and computador == 'tesoura':
    print('COMPUTADOR!')
elif apostaJogador == 'tesoura' and computador == 'pedra':
    print('COMPUTADOR!')
elif apostaJogador == 'tesoura' and computador == 'papel':
    print('{}'.format(jogador))
else:
    print('NINGUÉM, EMPATOU.')
