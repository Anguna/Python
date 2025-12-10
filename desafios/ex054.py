from datetime import date
ano = 0
ano = date.today().year
idademaior = 0
idademenor = 0
for c in range(1,8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if (ano - nascimento) >= 18:
        idademaior += 1
    else:
        idademenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(idademaior))
print('E também tivemos {} pessoas menores de idade'.format(idademenor))
