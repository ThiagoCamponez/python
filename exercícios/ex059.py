primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
resultado = 0
opção = 0
sair = False
while sair == False:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('\n>>>>> Qual é a sua opção? '))
    if opção == 5:
        sair == True
    else:
        if opção == 1:
            resultado = primeiro + segundo
            print('\nO resultado da soma de {} + {} = {}'.format(primeiro, segundo, resultado))
        elif opção == 2:
            resultado = primeiro * segundo
            print('\nO resultado de {} x {} = {}'.format(primeiro, segundo, resultado))
        elif opção == 3:
            if primeiro > segundo:
                resultado = primeiro
            else:
                resultado = segundo
            print('Entre {} e {} o MAIOR é o {}!'.format(primeiro, segundo, resultado))
        elif opção == 4:
            print('\nInforme os novos números novamente:')
            primeiro = int(input('Primeiro valor: '))
            segundo = int(input('Segundo valor: '))
        print('=-=' * 12)
