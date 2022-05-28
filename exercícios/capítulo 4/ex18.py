print ('Digite o primeiro comprimento do triângulo.')
x = float(input())
print ('Digite o segundo comprimento do triângulo.')
y = float(input())
print ('Digite o terceiro comprimento do triângulo.')
z = float(input())

if x< y+z and y<x+z and z<x+y:
    if x == y and y== z and x==z:
        print ('Este é um triângulo equilátero.')
    else:
        if x != y and y!= z and x!=z:
            print ('Este é um triângulo escaleno.')
        else:
            print ('Este é um triângulo isósceles.')
else:
    print ('Não é um triângulo.')
            
