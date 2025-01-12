dias = float(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
resd = dias * 60
reskm = km * 0.15
res = resd + reskm
print('O total a pagar é de R${:.2f}'.format(res))