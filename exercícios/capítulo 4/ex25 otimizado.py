print ('Qual o ângulo em graus?')
angulo = float(input())


sentido = 'sem sentido'

if angulo >0:
    sentido = 'sentido anti-horário'
    
elif angulo < 0:
    sentido = 'sentido horário'
print(sentido)

if angulo <0:
    angulo = -angulo
    
voltas = int(angulo/360)
angulo = angulo - voltas*360    
print(voltas,'voltas')
    
quadrante = 0

if angulo > 0 and angulo < 90:
    quadrante = 1
elif angulo > 90 and angulo < 180:
    quadrante = 2
elif angulo > 180 and angulo < 270:
    quadrante = 3
elif angulo > 270 and angulo < 360:
    quadrante = 4
else:
    if angulo == 0:
        print('Eixo x>0')
    elif angulo == 90:
        print('Eixo y>0')
    elif angulo == 180:
        print('Eixo x<0')
    else:
        print('Eixo y<0')

if sentido == 'sentido horário':
    quadrante = 5 - quadrante
if quadrante !=0:
    print('Quadrante',quadrante)
