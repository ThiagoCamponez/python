print('\033[35m-=\033[m' * 20)
num = int(input('\033[33mDigite um número inteiro: \033[m'))
print('''\033[1;30;45mEscolha uma das bases para conversão:\033[m 
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('\033[33mSua opção: \033[m'))
if opção == 1:
    print('\033[4;34m{}\033[m convertido para BINÁRIO é igual a \033[33m{}\033[m'.format(num, bin(num) [2:]))
elif opção == 2:
    print('\033[4;34m{}\033[m convertido para OCTAL é igual a \033[33m{}\033[m'.format(num, oct(num) [2:]))
elif opção == 3:
    print('\033[4;34m{}\033[m convertido para HEXADECIMAL é igual a \033[33m{}\033[m'.format(num, hex(num) [2:]))
else:
    print('\033[4;30;41mOpção inválida!\033[m Tente novamente.')