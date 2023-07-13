from datetime import date
print('\033[32m* \033[m' * 15)
print('\033[34mAlistamento Militar\033[m'.center(36))
print('\033[32m* \033[m' * 15)
sexo = str(input('Sexo: Masculino ou Feminino: ')).strip().upper()
if sexo == 'FEMININO':
     print('\n\033[4;31mAviso:\033[m Você não é obrigada a fazer o alistamento Militar!')
anoNascimento = int(input('\nDigite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
if idade < 18:
    print('\nEm {}, você completa {} anos de idade! Ainda faltam {} anos para seu alistamento Militar.'.format(anoAtual, idade, 18 - idade))
elif idade == 18:
    print('\nEm {}, você completa {} anos de idade! Deve se alistar para o Serviço Militar obrigatório!'.format(anoAtual, idade))
else:
    print('\nEm {}, você completa {} anos de idade! Você deveria ter se alistado à {} anos atrás!'.format(anoAtual, idade, idade - 18))
