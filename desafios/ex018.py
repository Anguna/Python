import math
ang = float(input('digite o ângulo que você deseja: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O ângulo de {} tem o Seno de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(ang, tan))