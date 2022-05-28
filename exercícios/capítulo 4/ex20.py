print ('Digite o código entre 1 e 10.')
codigo = int(input())
if codigo < 1 or codigo > 10:
    print ('código inválido.')
else:
    print ('Digite o peso em quilos.')
    peso = float(input())
    print ('Digite o código do país, entre 1 e 3.')
    pais = int(input())

    if pais <1 or pais >3:
        print ('Código do país inválido.')
    else:
        pesograma = peso*1000
        print ('Peso, em gramas:', pesograma)

        if 1<=codigo and codigo<=4:
            preco = 10*pesograma
            print ('Preço do produto =', preco)
        else:
            if 5<=codigo and codigo<=7:
                 preco = 25*pesograma
                 print ('Preço do produto =', preco)
            else:
                 preco = 35*pesograma
                 print ('Preço do produto =', preco)

        if pais == 1:
            imposto = 0
            print ('Valor do imposto =', imposto)
        else:
            if pais == 2:
                imposto = 0.15*preco
                print ('Valor do imposto =', imposto)
            else:
                imposto = 0.25*preco
                print('Valor do imposto =', imposto)

        valor = preco + imposto
        print ('Valor total =', valor)
        
