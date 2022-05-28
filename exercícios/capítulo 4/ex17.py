print ('Digite a variável a diferente de 0')
a = float (input())
if a == 0:
    print ('Variável a tem que ser diferente de zero.')
else:
    print('Digite a variável b')
    b = float(input())
    print('Digite a variável c')
    c = float(input())

    delta = b**2 - 4*a*c

    if delta < 0:
        print('Não existe uma raiz real.')
    else:
        if delta == 0:
            x = (-b)/(2*a)
            print ('Existe uma raiz real =', x)
        else:
            x1 = (-b + delta**(1/2))/(2*a)
            x2 = (-b - delta**(1/2))/(2*a)
            print ('Existem duas raízes reais:', x1, ' e', x2)
