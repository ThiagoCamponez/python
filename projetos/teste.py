'''
nome
ano do nascimento
ano atual
pergunta
'''

while True:
    nome = str(input('Qual é o seu nome? '))
    print('Prazer em conhece-lo {}.' .format(nome))
    ano_nasc = int(input('Qual o ano do seu nascimento? '))
    ano_atual = int(input('Em que ano estamos mesmo? '))
    idade = ano_atual - ano_nasc
    print('Você se chama {}, nasceu no ano de {} e sua idade atual hoje é de {} anos.'.format(nome, ano_nasc, idade))
    resposta = str(input('Você deseja continuar?SIM[S]/NÃO[N] ')).upper().strip()[0]
    if resposta == 'N':
        break