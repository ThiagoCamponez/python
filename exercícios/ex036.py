casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Pagará em quantos anos? '))
parcela = casa / (anos * 12)
if parcela > salario:
    print('EMPRÉSTIMO NEGADO! O valor da ')