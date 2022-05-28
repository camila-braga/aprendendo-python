print('Qual o salário?')
salario = float(input())

if salario <= 300:
    aumento = salario*0.15
    salario = salario + aumento
    print('Aumento será de R${:.2f}'.format(aumento),'e o novo salário será de R${:.2f}'.format(salario),'.')
    
else:
    if salario > 300 and salario < 600:    
        aumento = salario*0.1
        salario = salario + aumento
        print('Aumento será de R${:.2f}'.format(aumento),'e o novo salário será de R${:.2f}'.format(salario),'.')

    elif salario >= 600 and salario <= 900:    
        aumento = salario*0.05
        salario = salario + aumento
        print('Aumento será de R${:.2f}'.format(aumento),'e o novo salário será de R${:.2f}'.format(salario),'.')

    elif salario > 900:    
        aumento = 0
        salario = salario + aumento
        print('Aumento será de R${:.2f}'.format(aumento),'e o novo salário será de R${:.2f}'.format(salario),'.')
