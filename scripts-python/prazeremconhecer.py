nome = input('Bom dia! Qual é o seu nome? ')
print ('Olá',nome,'! Pazer em te conhecer!')
anoN = input('Por favor, informe o ano em que você nasceu. ')
mesN = input('Qual mês você faz aniversário? ')
diaN = input('E por último, em qual dia você nasceu? ')
print('Então você nasceu em', diaN,'de', mesN,'de', anoN,',certo?')
anoAtual = int(input('Qual nosso ano atual mesmo? '))
idade = anoAtual - anoN
print('Então você tem', idade)
