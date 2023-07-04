'''Projeto:
Criar um tomador de tabuada automático para a Manuelly
Perguntar tabuada de qual número deseja.
Perguntar aleatóriamente as 10 x da tabuada do número informado.
Contar erros e acertos.
Imprimir erros e acertos.
Se acertou 100% parabenizar e perguntar se deseja fazer de outro número.
Se não acertou 100%, imprimir mensagem que deve estudar mais e imprimir a tabuada completa para estudar.
'''

from random import shuffle

n = int(input('Tabuada do: '))
certo = 0
errado = 0

p1 = int(input('{} x 1 = '.format(n)))
if p1 == n * 1:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p2 = int(input('{} x 2 = '.format(n)))
if p2 == n * 2:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p3 = int(input('{} x 3 = '.format(n)))
if p3 == n * 3:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p4 = int(input('{} x 4 = '.format(n)))
if p4 == n * 4:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p5 = int(input('{} x 5 = '.format(n)))
if p5 == n * 5:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p6 = int(input('{} x 6 = '.format(n)))
if p6 == n * 6:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p7 = int(input('{} x 7 = '.format(n)))
if p7 == n * 7:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p8 = int(input('{} x 8 = '.format(n)))
if p8 == n * 8:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p9 = int(input('{} x 9 = '.format(n)))
if p9 == n * 9:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

p10 = int(input('{} x 10 = '.format(n)))
if p10 == n * 10:
    print('Certo')
    certo += 1
else:
    print('Errado..')
    errado += 1

lista = [p1, p2, p3, p4, p5. p6, p7, p8, p9, p10]
escolhido = shuffle(lista)

print('Você acertou: {}'.format(certo))
print('E errou: {}'.format(errado))

if certo == 10:
    print('Parabéns!! Você acertou todas!')
else:
    print('Você não conseguiu acertar todas e deve estudar mais!')
    print('{} x 1= {}'.format(n, n * 1))
    print('{} x 2= {}'.format(n, n * 2))
    print('{} x 3= {}'.format(n, n * 3))
    print('{} x 4= {}'.format(n, n * 4))
    print('{} x 5= {}'.format(n, n * 5))
    print('{} x 6= {}'.format(n, n * 6))
    print('{} x 7= {}'.format(n, n * 7))
    print('{} x 8= {}'.format(n, n * 8))
    print('{} x 9= {}'.format(n, n * 9))
    print('{} x 10= {}'.format(n, n * 10))