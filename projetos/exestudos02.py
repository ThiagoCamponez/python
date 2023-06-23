# continuar = 'S'
# while continuar != 'N':
#     nota01 = float(input('Digite a primeira nota: '))
#     nota02 = float(input('Digite a segunda nota: '))
#     nota03 = float(input('Digite a terceira nota: '))
#     media = (nota01 + nota02 + nota03) / 3
#
#     if media >= 6:
#         print('Você foi aprovado com a média: {:.2f}'.format(media))
#     elif media >= 4:
#         print(('Você NÃO foi aprovado! Sua média foi: {}. Está de recuperação!'.format(media)))
#     else:
#         print('Sua média foi {}. E terá que refazer a matéria no próximo semestre!'.format(media))
#
#     continuar = str(input('Deseja calcular mais alguma média? ')).upper().strip()[0]
#     if continuar == 'N':
#         print('Até mais!')

num = int(input('Digite um número: '))
while num < 0 or num > 10 or num == 0:
    print('Número inválido! Tente novamente.')
    num = int(input('Digite um número: '))
# n = 1
# while n <= 10:
#     tabuada = num * n
#     print('{}x{}={}'.format(num, n, tabuada))
#     n += 1

for n in range(1,11,1):
    tabuada = num * n
    print('%dx%d=%d'%(num, n, tabuada))
