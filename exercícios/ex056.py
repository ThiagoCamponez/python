somaidade = 0
maiorIdade = 0
nomemaioridade = 0
mulheres = 0
idadefeminino = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p).center(10))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if idade != 0:
        somaidade += idade
        maioridade = idade
    if sexo == 'm' and idade > maioridade:
        maioridade = idade
        nomemaioridade = nome
    if sexo == 'f':
        mulheres += 1
        idadefeminino = idade
        if idade > idadefeminino:
            idadefeminino = idade
mediaidade = somaidade / 4
print('Média: {}'.format(mediaidade))
print('Homem mais velho tem {} anos e se chama {}'.format(maiorIdade, nomemaioridade))
print('Ao todo são {} mulheres com menos de {} anos'.format(mulheres, (idadefeminino - 1)))