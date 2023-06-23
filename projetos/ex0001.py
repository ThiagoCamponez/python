nome = input('Qual é o seu nome? ')
print('É um grande prazer em te conhecer, {}!' .format(nome))
anoNasc = int(input('{}, em que ano você nasceu? ' .format(nome)))
mesNasc = input('E em qual mês? ')
diaNasc = int(input('Qual dia? '))
anoAtual = int(input('Em qual ano estamos mesmo? '))
idade = anoAtual - anoNasc
print('Então você tem {} anos!' .format(idade))
resposta = input('E nasceu em {} de {} de {}, certo? sim/não ' .format(diaNasc, mesNasc, anoNasc)).upper()
