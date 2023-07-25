n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    c += 1
    soma += n
    if n == 999:
        n = 999
c -= 1
soma -= 999
print('Você digitou {} números e a soma entre eles foi {}'.format(c, soma))