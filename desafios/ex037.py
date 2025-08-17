num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Converte para BINARIO')
print('[ 2 ] Converte para OCTAL')
print('[ 3 ] Converte para HEXADECIMAL')
res = int(input('Sua opção: '))
if res == 1:
    numcon = bin(num)[2:]
    base = 'BINARIO'
elif res == 2:
    numcon = oct(num)[2:]
    base = 'OCTAL'
elif res == 3:
    numcon = hex(num)[2:]
    base = 'HEXADECIMAL'
print('{} convertido para {} é igual a {}'.format(num, base, numcon))

