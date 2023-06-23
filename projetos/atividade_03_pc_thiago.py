pessoas_entr = 0
resp_sim = 0
resp_nao = 0
femi_sim = 0
masc_nao = 0
continuar = 0

while continuar != 'N':
    sexo = str(input('Qual o sexo do intrevistado? (M/F)')).upper().strip()[0]
    idade = int(input('Qual a idade? '))
    resposta = str(input('Gostou do novo produto? (S/N/I): ')).upper().strip()[0]

    pessoas_entr += 1
    if resposta == 'S':
        resp_sim += 1
        if sexo == 'F':
            femi_sim += 1
    elif resposta == 'N':
        resp_nao += 1
        if sexo == 'M':
            masc_nao += 1

    continuar = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
    if continuar == 'N':
        print('Foram {} pessoas entrevistadas.'.format(pessoas_entr))
        print('{} Pessoas que disseram SIM.'.format(resp_sim))
        print('{} Pessoas que disseram NÃO.'.format(resp_nao))
        print('{} Mulheres que disseram SIM.'.format(femi_sim))
        print('{} Homens que disseram NÃO.'.format(masc_nao))
        break

