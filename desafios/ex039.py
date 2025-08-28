import datetime
nasc = int(input('Ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    falta = 18 - idade
    alistamento = ano + falta
    print('Ainda faltam {} anos para o alistamento'.format(falta))
    print('Seu alistamento será em {}'.format(alistamento))
else:
    foi = idade - 18
    alistamento = ano - foi
    print('Você já deveria ter se alistado há {} anos'.format(foi))
    print('Seu alistamento foi em {}.'.format(alistamento))


