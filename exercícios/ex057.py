sexo = ''
while sexo != 'M' in sexo:
    sexo = str(input('Digite seu sexo [ M / F ]: ')).strip().upper()
    if sexo != 'M' or 'F':
        print('Opção Inválida! Tente novamente.')