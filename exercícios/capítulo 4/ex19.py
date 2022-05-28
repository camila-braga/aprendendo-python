print ('Qual a altura?')
altura = float(input())
print ('Qual o peso?')
peso = float(input())

if altura < 1.2:
    if peso <=60:
        print ('Classificação A.')
    else:
        if 60 > peso and peso<= 90:
            print ('Classificação D')
        else:
            print ('Clasificação G')
else:
    if 1.2 >= altura and altura<= 1.70:
        if peso <=60:
            print ('Classificação B')
        else:
            if 60 > peso and altura<= 90:
                print ('Classificação E')
            else:
                print ('Classificação H')
    else:
        if peso <=60:
            print ('Classificação C')
        else:
            if 60 > peso and altura <= 90:
                print ('Classificação F')
            else:
                print ('Classificação I')
