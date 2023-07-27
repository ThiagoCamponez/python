print('=' * 40)
print('BANCO CAMPONÊZ'.center(40))
print('=' * 40)

cinquenta = vinte = dez = um = 0

valor = int(input('Qual valor quer sacar: R$'))

cinquenta = valor // 50
vinte = (valor % 50) // 20
dez = vinte % 20
um = dez // 1

print(f'Total de {cinquenta} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')
print('=' * 40)
print('Volte sempre ao BANCO CAMPONÊZ! Tenha um ótimo dia!')