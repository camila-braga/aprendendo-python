print('Qual o salário?')
salario = float(input())

if salario <= 300:
    salario = salario + 0.5*salario
    print('Novo salário será de R${:.2f}'.format(salario))
elif salario > 300 and salario <= 500:
        salario = salario + 0.4*salario
        print('Novo salário será de R${:.2f}'.format(salario))
elif salario > 500 and salario <= 700:
        salario = salario + 0.3*salario
        print('Novo salário será de R${:.2f}'.format(salario))
elif salario > 700 and salario <= 800:
        salario = salario + 0.2*salario
        print('Novo salário será de R${:.2f}'.format(salario))
elif salario > 800 and salario <= 1000:
        salario = salario + 0.1*salario
        print('Novo salário será de R${:.2f}'.format(salario))
elif salario > 1000:
        salario = salario + 0.05*salario
        print('Novo salário será de R${:.2f}'.format(salario))
