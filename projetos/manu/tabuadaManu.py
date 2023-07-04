'''Projeto:
Criar um tomador de tabuada automático para a Manuelly
Perguntar tabuada de qual número deseja.
Perguntar aleatóriamente as 10 x da tabuada do número informado.
Contar erros e acertos.
Imprimir erros e acertos.
Se acertou 100% parabenizar e perguntar se deseja fazer de outro número.
Se não acertou 100%, imprimir mensagem que deve estudar mais e imprimir a tabuada completa para estudar.
'''

import random

def tabuada():
    n = int(input('Seja bem vinda(o)! Tabuada do número: '))
    acertos = 0
    erros = 0

    num = list(range(1, 11))
    random.shuffle(num)

    for i in num:
        resposta = int(input('{} x {} = '.format(n, i)))
        resultado = n * i

        if resposta == resultado:
            print('Você acertou!')
            acertos += 1
        else:
            print('Você errou. O correto é {}'.format(resultado))
            erros += 1

    print('Acertou um total de: {}'.format(acertos))
    print('E errou um total de: {}'.format(erros))

    if acertos == 10:
        print('Parabéns!! Você acertou todas!\U0001F389 \U0001F3C6 \U0001F38A')
    else:
        print('Você não conseguiu acertar todas, então deverá estudar mais!')
        print("\nTabuada completa:")
        for i in range(1, 11):
            print('{} x {} = {}'.format(n, i, n * i))
tabuada()