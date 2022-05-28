import math
print('Qual o ângulo e a distância em que a escada está da parede?')
angulo = float(input())
dist = float(input())

radiano = math.radians(angulo)
escada = dist/math.cos(radiano)
print('O tamanho da escada deverá ser {:.2f}'.format(escada),'m.')
