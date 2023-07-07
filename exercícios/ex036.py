from time import sleep

print('\033[34m-\033[m' * 38)
print('\033[1;33m SIMULAÇÃO DE FINANCIAMENTO DE IMÓVEL\033[m')
print('\033[34m-\033[m' * 38)

casa = float(input('Valor do imóvel? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Parcelado em quantos anos? '))
quantParcelas = anos * 12
valorParcelas = casa / quantParcelas

print('\033[1;33mVERIFICANDO...\033[m')
sleep(2)

if valorParcelas >= salario * 30 / 100:
    print('\033[4;31mO valor da parcela excedeu o limite de 30% do seu salário.\nEmpréstimo NÃO LIBERADO!\033[m')
else:
    print('\033[4;32mOk, o empréstimo poderá ser liberado com {:.0f} x R${:.2f}\033[m'.format(quantParcelas, valorParcelas))
