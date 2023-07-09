print('*' * 20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('\033[4;30;45mO 1º número é maior\033[m')
elif n1 < n2:
    print('O 2º número é maior')
else:
    print('Os números são iguais!')