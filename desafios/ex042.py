a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b and a == b and b == c:
    print('Os segmentos acima PODEM FORMAR um triângulo Equilátero')
elif a < b + c and b < a + c and c < a + b and a == b or b == c or a == c:
    print('Os segmentos acima PODEM FORMAR um triângulo Isósceles')
elif a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
