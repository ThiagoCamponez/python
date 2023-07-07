from time import sleep
print('\033[34m-\033[m' * 38)
print('\033[1;33m SIMULAÇÃO DE FINANCIAMENTO DE IMÓVEL\033[m')
print('\033[34m-\033[m' * 38)
casa = float(input('Valor do imóvel? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Parcelado em quantos anos? '))
parcela = casa / (anos * 12)
print('\033[1;33mVERIFICANDO...\033[m')
sleep(2)
if parcela >= salario * 30 / 100:
    print('\033[4;31mInfelizmente você não pode receber o empréstimo\033[m')
else:
    print('\033[4;32mOk, o empréstimo será liberado\033[m')