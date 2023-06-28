salarioAtual = float(input('Qual o valor do salário? R$'))
novoSalario = salarioAtual + (salarioAtual * 15 / 100)
print('Seu salário com 15% de aumento ficará no valor de R${:.2f}'.format(novoSalario))