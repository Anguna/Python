from traceback import print_tb

a = input('Digite algo: ')

print('É do tipo', type(a))
print('Só tem espaços?', a.isspace())
print('É maiusculo?', a.isupper())
print('É minusculo?', a.islower())
print('É número?', a.isnumeric())
print('É alfabeto?', a.isalpha())