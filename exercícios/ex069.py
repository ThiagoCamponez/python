maiordeidade = 0
masculino = 0
feminino = 0
femininomenor = 0
while True:
    menor = 0
    print('-' * 30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        maiordeidade += 1
    elif idade < 18:
        menor += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1
    if menor > 1 and sexo == 'F':
        feminino += menor
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            masculino += 1
        elif sexo == 'F':
            feminino += 1
        if menor > 1 and sexo == 'F':
            feminino += menor
    print('-' * 30)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'======= FIM DO PROGRAMA ======='.center(30))
print(f'Total de pessoas com mais de 18 anos: {maiordeidade}')
print(f'Ao todo temos {masculino} homens cadastrados')
print(f'E temos {feminino} mulheres com menos de 20 anos')