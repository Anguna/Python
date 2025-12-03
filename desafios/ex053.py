frase = str(input('Digite uma frase: '))
mai = frase.upper()
sem = mai.replace(" ", "")
invertido = sem[::-1]
print('O invertido de {} é {}'.format(sem, invertido))
if sem == invertido:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
