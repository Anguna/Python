nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
if media >= 7:
    print('O aluno está APROVADO.')
elif media < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está de RECUPERAÇÃO')
