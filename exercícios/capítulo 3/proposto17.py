import math
print('Qual o raio?')
raio = float(input())

c = 2*math.pi*raio
print('O comprimento do círculo é',c,'m.')

area = math.pi*(raio**2)
print('A área é', area,'m².')

vol = 3*math.pi*(raio**3)/4
print('O volume é', vol, 'm³.')
