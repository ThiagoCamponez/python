print('-' * 30)
print('Analisador de Triângulos 2.0')
print('-' * 30)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos informados PODEM formar um Triângulo', end = ' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else: 
        print('ISÓSCELES')
else:
    print('Os segmentros acima NÃO podem formar um Triângulo')