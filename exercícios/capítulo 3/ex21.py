print('Qual o comprimento da escada, em metros?')
escada = float(input())
print('Qual a altura que o quadro será pregado, em metros?')
altura = float(input())

if escada > altura:
    distancia = ((escada**2)-(altura**2))**(1/2)
    print('A distância que a escada deve estar da parede é {:.2f}'.format(distancia))
else:
    print('A altura da escada deve ser maior que a altura que se deseja alcançar.')
          
