dis = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dis))
preço = dis * 0.5 if dis <= 200 else dis * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))