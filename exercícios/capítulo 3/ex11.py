print ('Digite um número maior que zero.')
numero = float(input())

if numero >0:
    numero2 = numero**2
    print(numero2)
    numero2 = numero**3
    print(numero2)
    numero2 = numero**(1/2)
    print (numero2)
    numero2 = numero**(1/3)
    print (numero2)
else:
    print ('Número digitado não é maior que zero.')
