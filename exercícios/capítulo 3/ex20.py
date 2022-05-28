import math

print('Qual a medida do ângulo, em graus?')
angulo = float(input())

radiano = math.radians(angulo)

print('Qual a altura da parede, em metros?')
parede = float(input())

escada = parede/math.sin(radiano)

print('A altura da escada é {:.2f}'.format(escada),'m.')
