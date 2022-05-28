print ('Qual o valor do depósito?')
deposito = float(input())

print ('Qual o valor da taxa de juros?')
juros = float(input())

juros = juros/100

rendimento = deposito*juros

print ('O valor do rendimento é', rendimento)

total = deposito + rendimento

print('e o valor total após o rendimento é', total)
