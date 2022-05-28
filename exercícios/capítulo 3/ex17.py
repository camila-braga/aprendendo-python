print ('Salário:')
salario = float(input())
print('Primeiro cheque:')
cheque1 = float(input())
print('Segundo cheque:')
cheque2 = float(input())

imposto1 = cheque1*0.38/100
imposto2 = cheque2*0.38/100

saldo = salario - cheque1 - imposto1 - cheque2 - imposto2

print('Saldo atual = {:.2f}'.format(saldo))
