from datetime import date
print('\033[34m-=\033[m' * 16)
print('\033[4;33mConfederação Nacional de Natação\033[m')
print('\033[34m-=\033[m' * 16)
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
if idade <= 9:
    print('{} Anos - Categoria: \033[35mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('{} Anos - Categoria: \033[36mINFANTIL\033[m'.format(idade))
elif idade <= 19:
    print('{} Anos - Categoria: \033[32mJUNIOR\033[m'.format(idade))
elif idade <= 20:
    print('{} Anos - Categoria: \033[34mSENIOR\033[m'.format(idade))
else:
    print('{} Anos - Categoria: \033[31mMASTER\033[m'.format(idade))