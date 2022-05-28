print('Digite as duas notas.')
nota1 = float(input())
nota2 = float(input())

med = (nota1+nota2)/2

if med>=0 and med<3:
    print('Reprovado.')
else:
    if med>=3 and med<7:
        print('Exame')
    else:
        print('Aprovado')


        
