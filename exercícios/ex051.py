print('=' * 30)
print('10 TERMOS DE UMA P. A.'.center(30))
print('=' * 30)
t1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = t1 + (10 - 1) * razao
for c in range(t1, decimo + razao, razao):
    print(c, end = ' → ')
print('ACABOU!')