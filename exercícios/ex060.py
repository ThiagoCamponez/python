# from math import factorial
# num = int(input('Digite um número para calcular seu Fatorial: '))
# fatorial = factorial(num)
# print('O fatorial de {} é {}.'.format(num, fatorial))

# num = int(input('\nDigite um número para calcular seu Fatorial: '))
# c = num           #c é o contador
# f = 1
# print('\nCalculando {}! = '.format(num), end='')
# while c > 0:
#     print('{}'.format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print('{}\n'.format(f))

num = int(input('Digite um número para calcular seu Fatorial: '))
print('\nCalculando o {}! = '.format(num), end='')
f = 1
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}\n'.format(f))