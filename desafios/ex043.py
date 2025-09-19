peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está muito Magro')
elif 18.5 < imc < 24.9:
    print('Você está com o peso Normal')
elif 25 <= imc < 29.9:
    print('Você está com Sobrepeso')
elif 30 <= imc < 34.9:
    print('Você está com Obesidade grau I')
elif 35 <= imc < 39.9:
    print('Você está com Obesidade grau II')
elif imc > 40:
    print('Você está com Obesidade grau III')
