print ('Qual o código de estado do caminhão? Número entre 1 e 5.')
estado = int(input())
if estado <1 or estado >5:
    print ('Código inválido.')
else:
    print('Qual o peso da carga, em toneladas')
    peso = float(input())
    print('Qual o código da carga? Número entre 10 e 40.')
    carga = int(input())
    if carga<10 or carga >40:
        print ('Código inválido.')
    else:
        quilo = 1000*peso
        print('Peso da carga em quilos =', quilo)
        if 10<=carga and carga <=20:
            preco = quilo*100
            print ('Preço =', preco)
        else:
            if 21<=carga and carga <=30:
                preco = quilo*250
                print ('Preço =', preco)
            else:
                preco = quilo*340
                print ('Preço =', preco)
        if estado ==1:
            imposto = 0.35*preco
            print ('Imposto =', imposto)
        else:
            if estado==2:
                imposto = 0.25*preco
                print ('Imposto =', imposto)
            else:
                if estado ==3:
                    imposto = 0.15*preco
                    print ('Imposto =', imposto)
                else:
                    if estado==4:
                        imposto = 0.05*preco
                        print ('Imposto =', imposto)
                    else:
                        imposto = 0
                        print ('Imposto =', imposto)
        valor = preco + imposto
        print ('Valor da carga =', valor)
                

        
