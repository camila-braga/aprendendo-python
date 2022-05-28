print('Digite 2 números')
a=float(input())
b=float(input())

print('Digite uma opção. Números inteiros de 1 a 3')
opcao = int(input())

if opcao != 1 or opcao!=2 or opcao!=3:
    print('Opção inválida.')
else:
    if opcao == 1:
        x = a**b
        print(x)
    elif opcao == 2:
        x = a**(1/2)
        y = b**(1/2)
        print(x)
        print(y)
    elif opcao ==3:
        x = a**(1/3)
        y = b**(1/3)
        print(x)
        print(y)
