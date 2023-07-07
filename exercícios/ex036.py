casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Pagará em quantos anos? '))
parcela = casa / (anos * 12)
if parcela >= salario * 30 / 100:
    print('Infelizmente você não pode receber o empréstimo')
else:
    print('Ok, o empréstimo será liberado')