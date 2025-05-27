import random
alum = str(input('Primeiro Aluno: '))
aldois = str(input('Segundo Aluno: '))
altres = str(input('Terceiro Aluno: '))
alquatro = str(input('Quarto Aluno: '))
lista = [alum, aldois, altres, alquatro]
sorteado = random.choice(lista)
print('O aluno escolhido foi {}'.format(sorteado))