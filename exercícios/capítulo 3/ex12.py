print ('Digite o primeiro número, maior que zero.')
numero1 = float(input())

if numero1 > 0:
    print('Digite o segundo número, maior que zero.')
    numero2 = float(input())
    if numero2 <= 0:
        print ('Número digitado não é maior que zero.')
    else:
        x = numero1**numero2
        print('O primeiro número elevado ao segundo é,', x)
        x = numero2**numero1
        print('O segundo número elevado ao primeiro é,', x)
else:
    print('Número digitado não é maior que zero.')
