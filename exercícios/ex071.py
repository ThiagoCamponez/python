print('=' * 40)
print('BANCO CAMPONÊZ'.center(40))
print('=' * 40)
cinquenta = vinte = dez = um = 0
valor = int(input('Qual valor quer sacar: '))
cinquenta = valor // 50
vinte = ((valor % 50) / 20) // 50
dez = (valor % 50) / 10
print(f'Total de {cinquenta} notas de R$50')
print(f'Total de {vinte} notas de R$20')
print(f'Total de {dez} notas de R$10')