preço =float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x n cartão')
print('[ 4 ] 3x ou mais no cartão')
alternativa = int(input('Qual é a opção?'))
if alternativa == 1:
    valor = preço - ((preço * 10)/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, valor))
elif alternativa == 2:
    valor = preço - ((preço * 5)/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, valor))
elif alternativa == 3:
    valorparcelas = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(valorparcelas))
    print('Sua compra vai custar R${:.2f}.'.format(preço))
elif alternativa == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor = preço + ((preço * 20) / 100)
    valorparcelas = valor / parcelas
    print('Sua compra será parcelada em {:.2f}x de R${:.2f} COM JUROS'.format(parcelas, valorparcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, valor))
else:
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')

