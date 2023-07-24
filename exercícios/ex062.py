print('-=' * 10)
print('Gerador de PA'.center(20))
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 1
ntermos = 0
while mais != 0:
    while cont <= 10:
        print('{} → '.format(termo), end='')
        cont += 1
        termo += razão
        ntermos += mais
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    if mais != 0:
        while cont == mais:
            print('{} → '.format(termo), end='')
            cont += 1
            termo += razão
            ntermos += mais
print('Progressão finalizada com {} termos mostrados.'.format(ntermos))