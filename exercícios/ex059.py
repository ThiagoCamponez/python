from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
resultado = 0
opção = 0
sair = False
while opção != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('\n>>>>> Qual é a sua opção? '))
    sleep(1)
    if opção == 1:
        resultado = primeiro + segundo
        print('\nO resultado da soma de {} + {} = {}'.format(primeiro, segundo, resultado))
    elif opção == 2:
        resultado = primeiro * segundo
        print('\nO resultado de {} x {} = {}'.format(primeiro, segundo, resultado))
    elif opção == 3:
        if primeiro > segundo:
            resultado = primeiro
        elif segundo > primeiro:
            resultado = segundo
        else:
            print('\nSão IGUAIS!')            
        print('Entre {} e {} o MAIOR é o {}!'.format(primeiro, segundo, resultado))
    elif opção == 4:
        print('\nInforme os novos números novamente:')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando..')
    else:
        print('Opção Inválida! Tente novamente!')
    print('=-=' * 11)
    sleep(2)
print('Fim do programa! Volte sempre!')
print('=-=' * 11)