'''
primeira nota
segunta nota
soma
divisão
resultado
'''

aluno = str(input('Digite o nome do aluno: '))
pri = float(input('Digite a primeira nota de {}: '.format(aluno)))
seg = float(input('Digite a segunda nota de {}: ' .format(aluno)))
soma = pri + seg
nota = soma / 2
print('A média final de {} é: {:=^20}!' .format(aluno, nota))
