
print('Digite dois números quaisquer.')
n1 = float(input())
n2 = float(input())

print('Digite um número entre 1 e 4')

escolha = int(input())
if escolha!=1 or escolha!=2 or escolha!=3 or escolha!=4:
    print('Número inválido.')
else:
    if escolha == 1:
        x = (n1+n2)/2
        print('Média =',x)
    elif escolha ==2:
        if n1>n2:
            x = n1-n2
            print('Diferença =',x)
        else:
            x = n2-n1
            print('Diferença =', x)
    elif escolha ==3:
        x = n1*n2
        print('Produto =', x)

    elif escolha ==4:
       if n2!=0:
            x = n1/n2
            print('Divisão =',x)
       else:
            print('Impossível realizar a divisão.')

