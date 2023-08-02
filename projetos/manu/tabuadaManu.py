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
import time
from time import sleep

def tabuada():
    n = int(input('\033[4;30;45mSeja bem vinda(o)!\033[m Tabuada do número: '))
    acertos = 0
    erros = 0
    inicio = time.time()
    tempo_total = 0

    num = list(range(1, 11))
    random.shuffle(num)

    for i in num:
        resposta = int(input('{} x {} = '.format(n, i)))
        resultado = n * i

        if resposta == resultado:
            sleep(1)
            print('\033[1;32mVocê acertou!\033[m\U0001F389')
            acertos += 1
        else:
            print('\033[1;31mVocê errou.\033[m O correto é \033[1;32m{}\033[m'.format(resultado))
            erros += 1

    print('Acertou um total de: {}'.format(acertos))
    print('E errou um total de: {}'.format(erros))

    if acertos == 10:
        print('\033[1;32mParabéns!! Você acertou todas!\033[m\U0001F389 \U0001F3C6 \U0001F38A')
    else:
        print('Você não conseguiu acertar todas, então deverá estudar mais!')
        print("\nTabuada completa:")
        for i in range(1, 11):
            print('{} x {} = {}'.format(n, i, n * i))
    fim = time.time()
    tempo_total = fim - inicio
    if tempo_total < 60:
        print(f'Você terminou a tabuada em {tempo_total:.0f} segundos')
    else:
        print(f'Você terminou a tabuada em {tempo_total / 60:.2f} minutos')
tabuada()