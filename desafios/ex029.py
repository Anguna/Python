veloc = float(input('Qual é a velocidade atual do carro? '))
if veloc <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format((veloc - 80)*7))