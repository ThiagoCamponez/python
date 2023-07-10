from datetime import date
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - anoNascimento
if idade < 18:
    print('Você tem {} anos de idade! Ainda faltam {} anos para seu alistamento Militar.'.format(idade, 18 - idade))
elif idade == 18:
        print('Você tem {} anos de idade! Deve se alistar para o Serviço Militar obrigatório!'.format(idade))
else:
    print('Você tem {} anos de idade! Você deveria ter se alistado à {} anos atrás!'.format(idade, idade - 18))

