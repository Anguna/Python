import random
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
lista = [0, 1, 2, 3, 4, 5]
numero = random.choice(lista)
resposta = int(input('Em que número eu pensei? '))
if numero == resposta:
    print('Parabens! Você acertou!')
else:
    print('Errado! Eu pensei no {}'.format(numero))
