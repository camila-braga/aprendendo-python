print('Qual o salário?')
salario = float(input())

if salario <= 300:
    salario = salario + salario*0.35
    print('Salário reajustado é {:.2f}'.format(salario))
else:
    salario = salario + salario*0.15
    print('Salário reajustado é {:.2f}'.format(salario))
