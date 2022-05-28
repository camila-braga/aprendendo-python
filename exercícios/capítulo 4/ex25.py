print ('Qual o ângulo em graus?')
angulo = float(input())

if angulo >0:
    print('Sentido anti-horário')
    voltas = int(angulo/360)
    print('Quantidade de voltas completas:',voltas)
       
    if 0< angulo and angulo <90:
        print('Quadrante I')
    elif angulo ==90:
        print('Eixo y>0')
    elif 90<angulo and angulo <180:
        print('Quadrante II')
    elif angulo==180:
        print('Eixo x<0')
    elif 180<angulo and angulo<270:
        print('Quadrante III')
    elif angulo==270:
        print('Eixo y<0')
    elif 270<angulo and angulo<360:
        print('Quadrante IV')
    elif angulo==360 or angulo==0:
        print('Eixo x>0')
    elif angulo > 360:
        a = angulo - voltas*360
        if 0< a and a <90:
            print('Quadrante I')
        elif a==90:
            print('Eixo y>0')
        elif 90<a and a<180:
            print('Quadrante II')
        elif a==180:
            print('Eixo x<0')
        elif 180<a and a<270:
            print('Quadrante III')
        elif a==270:
            print('Eixo y<0')
        elif 270<a and a<360:
            print('Quadrante IV')
        elif a==360 or a==0:
            print('Eixo x>0')
        
else:
    if angulo == 0:
        print('Eixo x>0')
    elif:
        print('Sentido horário')
        voltas = int((-angulo)/360)
        print('Quantidade de voltas completas:',voltas)
                            
        if 0> angulo and angulo >-90:
            print('Quadrante IV')
        elif angulo ==-90:
            print('Eixo y<0')
        elif -90>angulo>-180:
            print('Quadrante III')
        elif angulo==-180:
            print('Eixo x<0')
        elif -180>angulo and angulo >-270:
            print('Quadrante II')
        elif angulo==-270:
            print('Eixo y>0')
        elif -270>angulo and angulo>-360:
            print('Quadrante I')
        elif angulo==-360:
            print('Eixo x>0')
        elif angulo < -360:
            a = angulo + voltas*360
            if 0> a and a>-90:
                print('Quadrante IV')
            elif a==-90:
                print('Eixo y<0')
            elif -90>a and a>-180:
                print('Quadrante III')
            elif a==-180:
                print('Eixo x<0')
            elif -180>a and a>-270:
                print('Quadrante II')
            elif a==-270:
                print('Eixo y>0')
            elif -270>a and a>-360:
                print('Quadrante I')
            elif a==-360 or a==0:
                print('Eixo x>0')
    


    
