from random import randint
print('Sou seu computador...')
ten = 1
comp = randint(0,10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
op = int(input('Qual é seu palpite?'))
while not comp == op:
    ten = ten + 1
    if op < comp:
        print('Mais... Tente mais uma vez')
    if op > comp:
        print('Menos... Tente mais uma vez')
    op = int(input('Qual é seu palpite?'))
print('Acertou com {} tentativas. Parabéns!'.format(ten))