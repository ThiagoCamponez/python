n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[31mALUNO REPROVADO!\033[m Média {}'.format(media))
elif media > 5 and media < 6.9:
    print('\033[33mALUNO EM RECUPERAÇÃO!\033[m Média {}'.format(media))
else:
    print('\033[32mALUNO APROVADO!\033[m Média {}'.format(media))